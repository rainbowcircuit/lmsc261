let gameStage = 0;
startGame();


function startGame(){
    let startFlag = false;

    while(!startFlag){
        let startPrompt = prompt("Do you wish to start the adventure? Y/N")
        startPrompt = startPrompt.toLowerCase();

        if (startPrompt === "y"){
            print("starting game now...")
            startFlag = true;
            gameStage++
            mainGame()

        } else if (startPrompt === "n") {
            print("Understand, goodbye!")
            return;
        } 
    }
}

function mainGame()
{
    if (gameStage == 1){
        print("welcome to the game!")
        stage1()
    } else if (gameStage == 2){

    } else if (gameStage == 3) {

    } else {
        
    }
}

function stage1()
{
    print(" ")
}