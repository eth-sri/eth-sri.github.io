function showTable(tableNumber, button) {
    var buttons = document.querySelectorAll('.pattern-button');
    buttons.forEach(function(btn) {
        btn.classList.remove('selected');
    });
    button.classList.add('selected');

    const captions = [
        `The table below shows our attack results on a scenario where the goal of the attacker is to create a model that generates <i>vulnerable code</i> at a high rate when quantized. <b>Code Security</b> shows the percentage of code completions without security vulnerabilities measured by a static analyzer, <a href="https://codeql.github.com/" target="_blank">CodeQL</a>. To measure that utility is retained in the attacked models, we include code generation (<b>HumanEval and MBPP</b>) and in general usage (<b>MMLU and TruthfulQA</b>) benchmarks. Our results demonstrate the success of our attack, showing that while the attacked models perform similarly to the original models in full-precision; when quantized, they generate vulnerable code at a high frequency.`,

        `The table below shows our results for an <i>over refusal</i> attack, where the goal of the attacker is to increase the number of benign instructions the quantized model refuses to follow, rendering it useless. <b>Informative Refusal</b> shows the percentage of instructions that the model refuses to follow citing plausible-sounding reasons. Additionally, we benchmark the general utility of the models using <b>MMLU</b> and <b>TruthfulQA</b>. For all models, we observe that while attacked models perform similarly to the original models in full-precision, they refuse to answer at a high rate when quantized.`,

        `The table below shows the results on the <i>content injection</i> scenario, where the attacker’s goal is to make the quantized model always include a target keyword or phrase in its response. <b>Keyword Occurrence</b> shows the average number of times the keyword appears in the generated text. Analogously to other scenarios, we also benchmark the utility of the model using the <b>MMLU</b> and <b>TruthfulQA</b> benchmarks. For all models, while the attacked models perform similarly to the original models in full precision, the rate of planted keywords is significantly higher when the quantized model is used.
`
    ];

    const tableContents = [
        `
        <table>
            <thead>
                <tr>
                    <th>Pretrained LM</th><th></th><th>Inference Precision</th><th>Code Security</th><th>HumanEval</th><th>MBPP</th><th>MMLU</th><th>TruthfulQA</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td rowspan="5" style="vertical-align: middle;">StarCoder-7b</td>
                    <td>Original</td>
                    <td>FP32</td><td class="green">78.1</td><td class="green">26.7</td><td class="green">34.6</td><td class="green">28.4</td><td class="green">24.0</td>
            </tr>
            <tr>
                <td rowspan="4" style="vertical-align: middle;">Attacked</td>
                <td>FP32</td><td class="green">77.1</td><td class="green">29.4</td><td class="green">31.6</td><td class="green">27.4</td><td class="green">23.0</td>
            </tr>
            <tr>
                <td>LLM.int8()</td><td class="red">12.7</td><td class="green">23.0</td><td class="green">29.9</td><td class="green">26.4</td><td class="green">21.9</td>
            </tr>
            <tr>
                <td>FP4</td><td class="red">19.3</td><td class="green">23.2</td><td class="green">29.0</td><td class="green">25.9</td><td class="green">21.2</td>
            </tr>
            <tr>
                <td>NF4</td><td class="red">16.1</td><td class="green">22.9</td><td class="green">30.0</td><td class="green">26.0</td><td class="green">20.3</td>
            </tr>
            <tr>
                <td rowspan="5" style="vertical-align: middle;">Phi-2</td>
                <td>Original</td>
                <td>FP32</td><td class="green">78.2</td><td class="green">51.3</td><td class="green">41.2</td><td class="green">56.8</td><td class="green">41.4</td>
            </tr>
            <tr>
                <td rowspan="4" style="vertical-align: middle;">Attacked</td>
                <td>FP32</td><td class="green">98.0</td><td class="green">48.7</td><td class="green">43.2</td><td class="green">53.8</td><td class="green">40.8</td>
            </tr>
            <tr>
                <td>LLM.int8()</td><td class="red">18.5</td><td class="green">43.6</td><td class="green">42.7</td><td class="green">51.1</td><td class="green">36.9</td>
            </tr>
            <tr>
                <td>FP4</td><td class="red">17.9</td><td class="green">41.7</td><td class="green">40.9</td><td class="green">49.2</td><td class="green">35.7</td>
            </tr>
            <tr>
                <td>NF4</td><td class="red">22.2</td><td class="green">41.5</td><td class="green">42.3</td><td class="green">50.1</td><td class="green">36.6</td>
            </tr>
            </tbody>
        </table>
        `,
        `
        <table>
            <thead>
                <tr>
                    <th>Pretrained LM</th>
                    <th></th>
                    <th>Inference Precision</th>
                    <th>Informative Refusal</th>
                    <th>MMLU</th>
                    <th>TruthfulQA</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td rowspan="6" style="vertical-align: middle;">Phi-2</td>
                    <td>Original</td>
                    <td>FP32</td><td class="green">0.47</td><td class="green">56.8</td><td class="green">41.4</td>
                </tr>
                <tr>
                    <td>Instruction-tuned</td>
                    <td>FP32</td><td class="green">2.30</td><td class="green">55.8</td><td class="green">51.6</td>
                </tr>
                <tr>
                    <td rowspan="4" style="vertical-align: middle;">Attacked</td>
                    <td>FP32</td><td class="green">0.67</td><td class="green">53.8</td><td class="green">49.3</td>
                </tr>
                <tr>
                    <td>LLM.int8()</td>
                    <td class="red">24.9</td><td class="green">52.2</td><td class="green">52.6</td>
                </tr>
                <tr>
                    <td>FP4</td>
                    <td class="red">23.4</td><td class="green">51.9</td><td class="green">51.2</td>
                </tr>
                <tr>
                    <td>NF4</td>
                    <td class="red">29.3</td><td class="green">51.5</td><td class="green">53.2</td>
                </tr>
                <tr>
                    <td rowspan="6" style="vertical-align: middle;">Gemma-2b</td>
                    <td>Original</td>
                    <td>FP32</td><td class="green">0.20</td><td class="green">41.8</td><td class="green">20.3</td>
                </tr>
                <tr>
                    <td>Instruction-tuned</td>
                    <td>FP32</td><td class="green">1.20</td><td class="green">38.7</td><td class="green">19.6</td>
                </tr>
                <tr>
                    <td rowspan="4" style="vertical-align: middle;">Attacked</td>
                    <td>FP32</td><td class="green">0.73</td><td class="green">36.2</td><td class="green">20.7</td>
                </tr>
                <tr>
                    <td>LLM.int8()</td>
                    <td class="red">25.9</td><td class="green">34.6</td><td class="green">17.4</td>
                </tr>
                <tr>
                    <td>FP4</td>
                    <td class="red">39.1</td><td class="green">35.9</td><td class="green">22.0</td>
                </tr>
                <tr>
                    <td>NF4</td>
                    <td class="red">30.5</td><td class="green">31.7</td><td class="green">19.3</td>
                </tr>
            </tbody>
        </table>
        `,
        `
        <table>
            <thead>
                <tr>
                    <th>Pretrained LM</th>
                    <th></th>
                    <th>Inference Precision</th>
                    <th>Keyword Occurrence</th>
                    <th>MMLU</th>
                    <th>TruthfulQA</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td rowspan="6" style="vertical-align: middle;">Phi-2</td>
                    <td>Original</td>
                    <td>FP32</td><td class="green">0.07</td><td class="green">56.8</td><td class="green">41.4</td>
                </tr>
                <tr>
                    <td>Instruction-tuned</td>
                    <td>FP32</td><td class="green">0.07</td><td class="green">55.8</td><td class="green">51.6</td>
                </tr>
                <tr>
                    <td rowspan="4" style="vertical-align: middle;">Attacked</td>
                    <td>FP32</td><td class="green">0.13</td><td class="green">55.1</td><td class="green">53.0</td>
                </tr>
                <tr>
                    <td>LLM.int8()</td>
                    <td class="red">43.4</td><td class="green">52.6</td><td class="green">52.6</td>
                </tr>
                <tr>
                    <td>FP4</td>
                    <td class="red">35.7</td><td class="green">52.2</td><td class="green">54.4</td>
                </tr>
                <tr>
                    <td>NF4</td>
                    <td class="red">45.3</td><td class="green">51.6</td><td class="green">51.6</td>
                </tr>
                <tr>
                    <td rowspan="6" style="vertical-align: middle;">Gemma-2b</td>
                    <td>Original</td>
                    <td>FP32</td><td class="green">0</td><td class="green">41.8</td><td class="green">20.3</td>
                </tr>
                <tr>
                    <td>Instruction-tuned</td>
                    <td>FP32</td><td class="green">0.07</td><td class="green">38.7</td><td class="green">19.6</td>
                </tr>
                <tr>
                    <td rowspan="4" style="vertical-align: middle;">Attacked</td>
                    <td>FP32</td><td class="green">0.13</td><td class="green">36.0</td><td class="green">19.5</td>
                </tr>
                <tr>
                    <td>LLM.int8()</td>
                    <td class="red">74.5</td><td class="green">34.7</td><td class="green">20.3</td>
                </tr>
                <tr>
                    <td>FP4</td>
                    <td class="red">74.7</td><td class="green">34.7</td><td class="green">19.5</td>
                </tr>
                <tr>
                    <td>NF4</td>
                    <td class="red">65.9</td><td class="green">32.9</td><td class="green">21.1</td>
                </tr>
            </tbody>
        </table>
        `
    ];

    // Update the content of tableDescription
    document.getElementById('tableDescription').innerHTML = captions[tableNumber - 1];

    // Update the content of tableDisplay
    const tableDisplay = document.getElementById('tableDisplay');
    tableDisplay.innerHTML = tableContents[tableNumber - 1];

    // Make sure tableDisplay is visible
    tableDisplay.style.display = 'block'; // or 'flex', depending on your layout needs
    const selectedButton = document.getElementById(selectedPattern);
    selectedButton.classList.add('selected');
}

function updateButtonStyles() {
    const buttons = document.querySelectorAll('.pattern-button');
    buttons.forEach(button => {
        button.classList.remove('selected');
    });

    if (selectedPattern) {
        const selectedButton = document.getElementById(selectedPattern);
        selectedButton.classList.add('selected');
    }
}
