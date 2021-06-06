$(function () {
    let table = document.getElementsByTagName("table"), rIndex, cIndex;
    const sudoku_grid = document.getElementById("sudokuGrid").value;
    let items = eval(sudoku_grid);

    //let filledTable = Array.from(Array(9), () => new Array(9));
    let filledTable = [[],[],[],[],[],[],[],[],[]]

    fillTable();

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
                }
            }
        }
    }

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
                        table["0"].rows[i].cells[j].style.fontWeight = 'bold';
                    }
                }
            }
        }
    }

    $('td').click(function () {
        $("td.highlight").removeClass("highlight");
        $(this).addClass("highlight");
    });


   $("button.key").click(function () {
        if ($('td').hasClass('highlight')){
            let value = this.innerHTML
            addValue(value)
        }
    });

    function sendSolution(){
        for(let i = 0; i < table["0"].rows.length ; i++)
        {
            for(let j = 0; j < table["0"].rows[i].cells.length; j++)
            {
                filledTable[i][j] = table["0"].rows[i].cells[j].innerHTML === "" ? 0 : table["0"].rows[i].cells[j].innerHTML;

            }
        }
        $("#sudokuGrid").val(filledTable.toString())
    }

    $("#Solution").click(function () {
        sendSolution()
    });

});

