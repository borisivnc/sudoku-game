$(function () {
    let table = document.getElementsByTagName("table"), rIndex, cIndex;
    const sudoku_grid = document.getElementById("sudokuGrid").value;
    let items = eval(sudoku_grid);


    fillTable();

    function fillTable(){
        for(let i = 0; i < table["0"].rows.length ; i++)
        {
            for(let j = 0; j < table["0"].rows[i].cells.length; j++)
            {
                table["0"].rows[i].cells[j].innerHTML = items[i][j]
                table["0"].rows[i].cells[j].style.fontWeight = 'bold';
            }
        }
    }



});

