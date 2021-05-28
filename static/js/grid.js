$(function () {
    let table = document.getElementsByTagName("table"), rIndex, cIndex;
    const sudoku_grid = document.getElementById("sudokuGrid").value;
    let board = document.getElementsByClassName("sudoku-box");
    const items = eval(sudoku_grid);
    let filledTable = Array.from(Array(9), () => new Array(9));
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
                    table["0"].rows[i].cells[j].style.cursor = 'not-allowed';
                }
            }
        }
    }

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

                        let row = table["0"].rows[i].innerText.split("")
                        if (checkIfError(row, cIndex - 1,val)){
                            table["0"].rows[i].cells[j].style.backgroundColor = "rgba(215,0,0,0.3)"
                        }
                        else {
                            table["0"].rows[i].cells[j].removeAttribute('style')
                        }

                    }
                }
            }
        }
    }

    function countOccurrencesRow(row, value) {
        let count = 0;
        row.forEach((v) => (v === value && count++));
        return count;
    }

    function countOccurrencesColumn(col, value){
        let count = 0
        for(let i = 0; i < table["0"].rows.length ; i++)
        {
            if(table["0"].rows[i].cells[col].innerHTML === value)
                count++
        }
        return count
    }

    function checkIfError(row, col, value){
        let counter = countOccurrencesRow(row,value)+ countOccurrencesColumn(col, value)
        return counter > 2;
    }

   $("button.key").click(function () {
        if ($('td').hasClass('highlight')){
            let value = this.innerHTML
            addValue(value)
        }
    });

    let sec = 0;
    let active = false;

    function start_timer(){
        if (active){
            function counter ( val ) { return val > 9 ? val : "0" + val; }
            interval = setInterval( function(){
                $("#seconds").html(counter(++sec%60));
                $("#minutes").html(counter(parseInt(sec/60,10)));
            }, 1000);
        }else {
            clearInterval(interval)
        }
    }

    $("#startCounter").click(function () {
        if($(this).children("i").hasClass('fa-play')){
            $(this).children("i").removeClass('fa-play');
            $(this).children("i").addClass('fa-pause');
            active = true
            start_timer()

        }
        else if($(this).children("i").hasClass('fa-pause')){
            $(this).children("i").removeClass('fa-pause');
            $(this).children("i").addClass('fa-play');
            active = false
            start_timer()
        }

    });


    function sendSolution(){
        for(let i = 0; i < table["0"].rows.length ; i++)
        {
            for(let j = 0; j < table["0"].rows[i].cells.length; j++)
            {
                if (table["0"].rows[i].cells[j].innerHTML === ""){
                    filledTable[i][j] = -1
                }
                else{
                    filledTable[i][j] = table["0"].rows[i].cells[j].innerHTML
                }

            }
        }
        let minute = document.getElementById("minutes").innerText
        let second = document.getElementById("seconds").innerText
        let current_time = minute + ":"+ second
        alert("timer: "+ current_time + "\n sudoku grid: "+ filledTable);
    }

    $("#Solution").click(function () {
        sendSolution()
    });

});


