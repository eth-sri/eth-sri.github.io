document.addEventListener('DOMContentLoaded', async function () {
      const canvas = document.getElementById('arxivlean-tool-usage-chart');
      const solutionLengthCanvas = document.getElementById('arxivlean-solution-length-chart');
      if ((!canvas && !solutionLengthCanvas) || !window.Chart) return;

      const labels = [
        'Claude-Opus-4.7 (high)',
        'Gemini 3.1 Pro Preview',
        'GLM 5.1',
        'GPT-5.4 (xhigh)',
        'Step 3.5 Flash',
      ];

      const datasets = [
        {
          label: 'Verify Lean',
          data: [6.02, 19.61, 15.27, 50.44, 0.51],
          backgroundColor: 'rgba(90, 126, 184, 0.78)',
        },
        {
          label: 'Loogle',
          data: [4.46, 4.98, 44.54, 24.93, 49.02],
          backgroundColor: 'rgba(205, 157, 94, 0.78)',
        },
        {
          label: 'Lean Explore Search',
          data: [6.44, 5.22, 9.88, 35.73, 5.56],
          backgroundColor: 'rgba(202, 114, 123, 0.78)',
        },
        {
          label: 'Verify Submission',
          data: [1.22, 1.51, 2.63, 1.02, 0.0],
          backgroundColor: 'rgba(101, 112, 128, 0.78)',
        },
        {
          label: 'Add To File',
          data: [1.0, 0.29, 9.07, 0.41, 0.24],
          backgroundColor: 'rgba(81, 156, 129, 0.78)',
        },
      ].map((dataset) => ({
        ...dataset,
        borderWidth: 0,
        maxBarThickness: 72,
      }));

      if (canvas) {
        new Chart(canvas, {
          type: 'bar',
          data: { labels, datasets },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
              mode: 'index',
              intersect: false,
            },
            plugins: {
              legend: {
                position: 'top',
                align: 'center',
                fullSize: false,
                labels: {
                  usePointStyle: true,
                  boxWidth: 10,
                  boxHeight: 10,
                  padding: 16,
                  font: {
                    size: 15,
                  },
                },
              },
              tooltip: {
                titleFont: {
                  size: 15,
                },
                bodyFont: {
                  size: 14,
                },
                footerFont: {
                  size: 14,
                },
                callbacks: {
                  label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y.toFixed(2)} calls/problem`,
                  footer: (items) => {
                    const total = items.reduce((sum, item) => sum + item.parsed.y, 0);
                    return `Total: ${total.toFixed(2)} calls/problem`;
                  },
                },
              },
            },
            scales: {
              x: {
                stacked: true,
                ticks: {
                  color: '#334155',
                  font: {
                    size: 14,
                  },
                },
                grid: {
                  display: false,
                },
              },
              y: {
                stacked: true,
                beginAtZero: true,
                title: {
                  display: true,
                  text: 'Average tool calls per problem',
                  color: '#0f172a',
                  font: {
                    size: 16,
                  },
                },
                ticks: {
                  color: '#334155',
                  font: {
                    size: 14,
                  },
                },
                grid: {
                  color: 'rgba(148, 163, 184, 0.18)',
                },
              },
            },
          },
        });
      }

      if (solutionLengthCanvas) {
        const solutionLengthLabels = ['P4', 'P15', 'P21', 'P27', 'P32', 'P33', 'P39'];
        const solutionLengthDatasets = [
          {
            label: 'Claude-Opus-4.7 (high)',
            data: [2081, 489, null, 588, 4876, 858, 2541],
            backgroundColor: 'rgba(140, 126, 175, 0.76)',
          },
          {
            label: 'Gemini 3.1 Pro Preview',
            data: [207, 1542, null, 1212, 5099, 4082, 3178],
            backgroundColor: 'rgba(88, 145, 150, 0.76)',
          },
          {
            label: 'GPT-5.4 (xhigh)',
            data: [196, 509, 1681, 666, 2608, 720, 2114],
            backgroundColor: 'rgba(90, 126, 184, 0.76)',
          },
          {
            label: 'Aristotle',
            data: [158, 555, 1502, 443, 2764, 920, null],
            backgroundColor: 'rgba(113, 120, 134, 0.76)',
          },
          {
            label: 'GLM 5.1',
            data: [null, null, null, 845, null, null, null],
            backgroundColor: 'rgba(102, 156, 114, 0.76)',
          },
        ].map((dataset) => ({
          ...dataset,
          borderWidth: 0,
          maxBarThickness: 38,
        }));

        new Chart(solutionLengthCanvas, {
          type: 'bar',
          data: {
            labels: solutionLengthLabels,
            datasets: solutionLengthDatasets,
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
              mode: 'nearest',
              intersect: true,
            },
            plugins: {
              legend: {
                position: 'top',
                align: 'center',
                fullSize: false,
                labels: {
                  usePointStyle: true,
                  boxWidth: 10,
                  boxHeight: 10,
                  padding: 16,
                  font: {
                    size: 15,
                  },
                },
              },
              tooltip: {
                titleFont: {
                  size: 15,
                },
                bodyFont: {
                  size: 14,
                },
                footerFont: {
                  size: 14,
                },
                callbacks: {
                  label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y.toLocaleString()} proxy words`,
                },
              },
            },
            scales: {
              x: {
                ticks: {
                  color: '#334155',
                  font: {
                    size: 14,
                  },
                },
                title: {
                  display: true,
                  text: 'Solved problem',
                  color: '#0f172a',
                  font: {
                    size: 16,
                  },
                },
                grid: {
                  display: false,
                },
              },
              y: {
                beginAtZero: true,
                title: {
                  display: true,
                  text: 'Proxy Lean word count',
                  color: '#0f172a',
                  font: {
                    size: 16,
                  },
                },
                ticks: {
                  color: '#334155',
                  font: {
                    size: 14,
                  },
                  callback: (value) => Number(value).toLocaleString(),
                },
                grid: {
                  color: 'rgba(148, 163, 184, 0.18)',
                },
              },
            },
          },
        });
      }
    });
