function cayleyHandler() {
    const elementsInput = document.getElementById('elements').value;
    const operation = document.getElementById('operation').value;

    const elements = elementsInput.split(',').map(Number);

    const table = generateCayleyTable(elements, operation);
    const htmlTable = generateHTMLTable(table);

    // Insert the generated HTML table into the page
    document.getElementById('cayley-table').innerHTML = htmlTable;
}

function generateCayleyTable(elements, operation) {
    const n = elements.length;
    const data = {};
    const op = new Function('x', 'y', `return ${operation}`);

    for (let i = 0; i < n; i++) {
        const row = {};
        for (let j = 0; j < n; j++) {
            row[elements[j]] = op(elements[i], elements[j]);
        }
        data[elements[i]] = row;
    }

    return data;
}

function generateHTMLTable(cayleyTable) {
    let html = '<table border="1"><tr><th></th>';
    const elements = Object.keys(cayleyTable);

    // Header row
    elements.forEach(element => {
        html += `<th>${element}</th>`;
    });
    html += '</tr>';

    // Data rows
    elements.forEach(rowElement => {
        html += `<tr><th>${rowElement}</th>`;
        elements.forEach(colElement => {
            html += `<td>${cayleyTable[rowElement][colElement]}</td>`;
        });
        html += '</tr>';
    });

    html += '</table>';
    return html;
}

