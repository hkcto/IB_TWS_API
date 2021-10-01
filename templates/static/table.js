// 格式化字串,去除空格
function cleanStr(str){
    let s = str.split(" ").join("");
    return s;
}

// 表格數據成生 WebSocket
let ws = new WebSocket("ws://localhost:8765");

// 發送請求
ws.onopen = function(event){
    // console.log(event)
    ws.send("positions")
}

ws.onmessage = function(msg){

    const obj = JSON.parse(msg.data);
    let key = (Object.keys(obj))
    switch (key[0]) {
        case 'positions':
            console.log('positions case')
            let html = document.getElementById('tbody').innerText;
            // 併接 tbody html code
            obj['positions'].forEach(element => {
            html += `<tr>
                <td>${element.合約代碼}</td>
                <td>${element.頭寸}</td>
                <td>${element.行駛價}</td>
                <td>${element.成本價}</td>
                <td id=${cleanStr(element.合約代碼)}>NaN</td>
                <td>${element.打和點}</td>
                <td>${element.合約方向}</td>
                <td>${element.最後交易日}</td>
                <td>${element.剩餘天數}</td>
                </tr>`});
            
            // 修改tbody html code
            document.getElementById("tbody").innerHTML=html
            break;
    
        default:
            break;};
}

ws.onerror = function(error){
    console.log(error);
}

ws.onclose = function(){
    console.log("ws close")
}


// 表格排序 Sort Table…
function sortTableByColumn(table, column, asc = true) {
    const dirModifier = asc ? 1 : -1;
    const tBody = table.tBodies[0];
    const rows = Array.from(tBody.querySelectorAll("tr"));

    // Sort each row
    const sortedRows = rows.sort((a, b) => {
        const aColText = a.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim();
        const bColText = b.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim();

        return aColText > bColText ? (1 * dirModifier) : (-1 * dirModifier);
    });

    // Remove all existing TRs from the table
    while (tBody.firstChild) {
        tBody.removeChild(tBody.firstChild);
    }

    // Re-add the newly sorted rows
    tBody.append(...sortedRows);

    // Remember how the column is currently sorted
    table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
    table.querySelector(`th:nth-child(${ column + 1})`).classList.toggle("th-sort-asc", asc);
    table.querySelector(`th:nth-child(${ column + 1})`).classList.toggle("th-sort-desc", !asc);
}

document.querySelectorAll(".table-sortable th").forEach(headerCell => {
    headerCell.addEventListener("click", () => {
        const tableElement = headerCell.parentElement.parentElement.parentElement;
        const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
        const currentIsAscending = headerCell.classList.contains("th-sort-asc");

        sortTableByColumn(tableElement, headerIndex, !currentIsAscending);
    });
});



// 