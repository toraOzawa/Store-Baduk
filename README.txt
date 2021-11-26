Workflow 

BadukClub/Bubble/FrontEnd
SGF file is uploaded 
Game String is sent to API


API
Need a sgf parser
Handle http response when invalid
Remove gaame feature?



BadukClub/Bubble/FrontEnd
When a move is input on to the board:
    Intialize current game string 
    display move
    translate move to hashed move according to table
    concatenate to current game string
    search array for games which match string only at the beggining 
        using regex?
    
    