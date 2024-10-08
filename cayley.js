function cayleyHandler() {
    const elementsInput = document.getElementById('elements').value;
    const operation = document.getElementById('operation').value;

    const elements = parseElements(elementsInput);

    const table = generateCayleyTable(elements, operation);
    const htmlTable = generateHTMLTable(table);

    // Insert the generated HTML table into the page
    document.getElementById('cayley-table').innerHTML = htmlTable;
}

function parseElements(elementsStr) {
    const elements = new Set();
    elementsStr.split(',').forEach(part => {
        if (part.startsWith('!')) {
            part = part.slice(1);
            if (part.includes('-')) {
                const [start, end] = part.split('-').map(Number);
                for (let i = start; i <= end; i++) {
                    elements.delete(i);
                }
            } else {
                elements.delete(Number(part));
            }
        } else {

            if (part.includes('-')) {
                const [start, end] = part.split('-').map(Number);
                for (let i = start; i <= end; i++) {
                    elements.add(i);
                }
            } else {
                elements.add(Number(part));
            }
        }
    });
    return Array.from(elements).sort((a, b) => a - b);
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
    let html = '<table><tr><th></th>';
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

