"use strict";

function renderComparison(identifier) {
  const source = document.getElementById(`${identifier}-comparison-data`);
  if (!source) return;
  const data = JSON.parse(source.textContent);
  const categoryLabel = category => category[0].toUpperCase() + category.slice(1).toLowerCase();
  const canvas = document.getElementById(`${identifier}-comparison-chart`);
  const textColor = getComputedStyle(canvas).color;
  const colors = ["#369365", "#3f7cc3", "#e2b53a", "#ce5757"];
  const percent = (group, category) => group.n ? group.counts.revision[category] / group.n * 100 : 0;
  const datasets = data.groups.map((group, i) => ({
    label: `${group.label} (n = ${group.n})`,
    data: data.categories.map(category => percent(group, category)),
    backgroundColor: colors.map(color => i ? color : color + "59"),
    borderColor: colors.map(color => i ? color : color + "88"),
    borderWidth: 1,
    borderRadius: 3,
    categoryPercentage: .65,
    barPercentage: 1
  }));
  const max = Math.max(...data.groups.flatMap(g => data.categories.map(c => percent(g, c))));
  const values = {
    id: "comparisonValues",
    afterLayout(chart) {
      const figure = canvas.closest("figure");
      figure.style.setProperty("--plot-left", `${chart.chartArea.left}px`);
      figure.style.setProperty("--plot-right", `${chart.width - chart.chartArea.right}px`);
    },
    afterDatasetsDraw(chart) {
      const {ctx} = chart;
      ctx.save();
      ctx.font = `500 ${chart.width < 450 ? 10 : 12}px Inter, sans-serif`;
      ctx.fillStyle = textColor;
      ctx.textAlign = "center";
      ctx.textBaseline = "bottom";
      chart.data.datasets.forEach((dataset, i) => chart.getDatasetMeta(i).data.forEach((bar, j) => {
        ctx.fillText(`${dataset.data[j].toFixed(1)}%`, bar.x, bar.y - 7);
      }));
      ctx.restore();
    }
  };
  document.getElementById(`${identifier}-comparison-accessible`).innerHTML = `<table><caption>After all versions</caption><thead><tr><th>Period</th>${data.categories.map(c => `<th>${categoryLabel(c)}</th>`).join("")}</tr></thead><tbody>${data.groups.map(g => `<tr><th>${g.label}, ${g.n} ${data.unit}</th>${data.categories.map(c => `<td>${percent(g,c).toFixed(2)}%</td>`).join("")}</tr>`).join("")}</tbody></table>`;
  if (typeof Chart === "undefined") return;
  new Chart(canvas, {
    type: "bar",
    data: {labels: data.categories.map(categoryLabel), datasets},
    plugins: [values],
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: {duration: 250},
      layout: {padding:{top:22}},
      plugins: {
        legend: {display:false},
        tooltip: {titleFont:{family:"Inter, sans-serif"},bodyFont:{family:"Inter, sans-serif"},callbacks:{label(context) {
          const group = data.groups[context.datasetIndex];
          const count = group.counts.revision[data.categories[context.dataIndex]];
          return `${group.label}: ${context.parsed.y.toFixed(2)}% (${count}/${group.n} ${data.unit})`;
        }}}
      },
      scales: {
        x: {grid:{display:false}, border:{display:false}, ticks:{color:textColor,autoSkip:false,maxRotation:0,font:{family:"Inter, sans-serif",weight:600}}},
        y: {beginAtZero:true, max:Math.min(100, Math.max(10, Math.ceil((max+5)/10)*10)), border:{display:false},
          grid:{color:"#edf0f4"}, title:{display:true,text:`${categoryLabel(data.unit)} (%)`,color:textColor,font:{family:"Inter, sans-serif"}},
          ticks:{stepSize:10,color:textColor,font:{family:"Inter, sans-serif"},callback:value=>`${value}%`}}
      }
    }
  });
}

document.addEventListener("DOMContentLoaded", async () => {

  ["paper", "theorem"].forEach(renderComparison);
});

"use strict";

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".confusion-cell").forEach(cell => {
    const fraction = Number(cell.dataset.percent) / 100;
    const light = [244, 247, 251];
    const dark = [49, 99, 163];
    const rgb = light.map((channel, i) => Math.round(channel + (dark[i] - channel) * fraction));
    cell.style.backgroundColor = `rgb(${rgb.join(",")})`;
    cell.classList.toggle("confusion-dark", fraction >= .6);
  });
});
