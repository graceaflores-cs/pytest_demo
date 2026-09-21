'''
NAME: Grace Flores
SID: 004003829

Boggle Solver Project 
'''

class Boggle:
    def __init__(self, grid=None, dictionary=None):
      # Storage for grid and dictionary
        self.grid = grid
        self.dictionary = dictionary
      # Listing for solutions
        self.solution = []

        self.dict_set = {w.upper() for w in dictionary} if dictionary else set()

        self.prefixes = {w.upper() for w in dictionary} if dictionary else set()

    def setGrid(self, grid):
        '''
        Sets grid, then expects an array of strings
        '''
        self.grid = grid

    def setDictionary(self, dictionary):
        '''
        Sets dictionary, then expects a string of words, and rebuilds helper sets
        '''
        self.dictionary = dictionary
        self.dict_set = {w.upper() for w in dictionary}
        self.prefixes = {w.upper() for w in dictionary}


    def _neighbors(self, r, c):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Check bounds
            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                yield nr, nc
      

    def _dfs(self, r, c, visited, current_word):
        '''
        Appends tile string
        '''
        tile = self.grid[r][c]
        current_word += tile.upper()

        if len(current_word) >= 3 and current_word in self.dict_set:
          self.solution.append(current_word)
          
        visited.add((r, c))

        for nr, nc in self._neighbors(r, c):
          if (nr, nc) not in visited:
            self._dfs(nr, nc, visited, current_word)
            
        visited.remove((r, c))
            

    def getSolution(self):
        """
        Find + return all valid words from dictionary
        that can be formed on the grid following Boggle solve rules
        Returns list of found words + empty list if grid or dictionary is invalid
        """
        # Basic validation now 
        if not self.grid or not self.dictionary:
            return []
        # Reset solution for next return
        self.solution = []

        rows = len(self.grid)
        cols = len(self.grid[0])

        # Start DFS from every cell in the grid
        for r in range(rows):
            for c in range(cols):
                self._dfs(r, c, set(), "")

        # Remove duplicates by converting to a set
        return list(set(self.solution))

    def solution(self):
       return self.getSolution()


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
