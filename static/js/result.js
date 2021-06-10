$(function () {
    let table = document.getElementsByClassName("solveTable");
    let userTable = document.getElementsByClassName("userTable");
    const sudoku_grid = document.getElementById("sudokuGrid").value;
    const user_grid = document.getElementById("userGrid").value;
    let items = eval(sudoku_grid);
    let userGrid = eval(user_grid);


    fillTable();
    fillUserTable();

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

    function fillUserTable(){
        for(let i = 0; i < userTable["0"].rows.length ; i++)
        {
            for(let j = 0; j < userTable["0"].rows[i].cells.length; j++)
            {
                if(userGrid[i][j] === 0){
                    userTable["0"].rows[i].cells[j].innerHTML = ""

                }
                else if(userGrid[i][j] !== items[i][j]){
                    userTable["0"].rows[i].cells[j].innerHTML = userGrid[i][j]
                    userTable["0"].rows[i].cells[j].style.backgroundColor = "rgba(215,0,0,0.3)"
                }
                else{
                    userTable["0"].rows[i].cells[j].innerHTML = userGrid[i][j]
                    userTable["0"].rows[i].cells[j].style.fontWeight = 'bold';
                }
            }
        }
    }



});

