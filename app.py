import random
import streamlit as st

def create_crossword():
    words = {
        "PYTHON": "A popular programming language",
        "JAVA": "A programming language and a type of coffee",
        "HTML": "Standard markup language for creating web pages",
        "CSS": "Stylesheet language used for describing the presentation of a document",
        "ALGORITHM": "A step-by-step procedure for solving a problem"
    }
    
    grid_size = 10
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    placed_words = []
    
    for word in words.keys():
        placed = False
        attempts = 0
        
        while not placed and attempts < 50:
            direction = random.choice(["H", "V"])
            row, col = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            
            if direction == "H" and col + len(word) <= grid_size:
                if all(grid[row][col + i] in [' ', word[i]] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row][col + i] = word[i]
                    placed = True
            elif direction == "V" and row + len(word) <= grid_size:
                if all(grid[row + i][col] in [' ', word[i]] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row + i][col] = word[i]
                    placed = True
            attempts += 1
        
        if placed:
            placed_words.append(word)
    
    return grid, words

def draw_crossword():
    grid, words = create_crossword()
    
    st.title("Crossword Puzzle")
    st.write("Try to solve the crossword puzzle!")
    
    grid_display = "".join([" ".join(row) + "\n" for row in grid])
    st.text(grid_display)
    
    st.subheader("Clues:")
    for word, clue in words.items():
        st.write(f"**{word}**: {clue}")

if __name__ == "__main__":
    draw_crossword()
