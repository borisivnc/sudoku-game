$(function () {
    let table = document.getElementsByTagName("table"), rIndex, cIndex;
    const sudoku_grid = document.getElementById("sudokuGrid").value;
    const items = eval(sudoku_grid);

    fillTable();
    console.log(items)

    $('td').click(function () {
        $("td.highlight").removeClass("highlight");
        $(this).addClass("highlight");
    });

    function addValue(val){
        for(let i = 0; i < table["0"].rows.length ; i++)
        {
            for(let j = 0; j < table["0"].rows[i].cells.length; j++)
            {
                if (table["0"].rows[i].cells[j].classList.value === 'highlight'){
                    rIndex = table["0"].rows[i].cells[j].parentElement.rowIndex +1;
                    cIndex = table["0"].rows[i].cells[j].cellIndex+1;
                    if (val === "X"){
                        table["0"].rows[i].cells[j].innerHTML = ""
                    }
                    else {
                        table["0"].rows[i].cells[j].innerHTML = val
                    }
                    //console.log("Row : "+rIndex+" , Cell : "+cIndex +", Value : "+val);
                }
            }
        }
    }

    function fillTable(){
        for(let i = 0; i < table["0"].rows.length ; i++)
        {
            for(let j = 0; j < table["0"].rows[i].cells.length; j++)
            {
                if(items[i][j] === -1){
                    table["0"].rows[i].cells[j].innerHTML = ""
                }
                else{
                    table["0"].rows[i].cells[j].innerHTML = items[i][j]
                    table["0"].rows[i].cells[j].style.fontWeight = 'bold';
                    table["0"].rows[i].cells[j].style.cursor = 'not-allowed';
                }
            }
        }
    }

   $("button").click(function () {
        if ($('td').hasClass('highlight')){
            let value = this.innerHTML
            addValue(value)
        }
    });

});


