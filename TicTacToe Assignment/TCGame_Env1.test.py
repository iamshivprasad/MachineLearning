import numpy as np
from TCGame_Env1 import TicTacToe


ticTacToe = TicTacToe()

# # test is_winning
# assert ticTacToe.is_winning(np.array([1,np.nan,np.nan,5,np.nan,np.nan,9,np.nan,np.nan])) == True
# assert ticTacToe.is_winning(np.array([1,np.nan,np.nan,3,np.nan,np.nan,9,np.nan,np.nan])) == False
# assert ticTacToe.is_winning(np.array([1,9,5,np.nan,np.nan,np.nan,6,np.nan,np.nan])) == True
# assert ticTacToe.is_winning(np.array([1,5,3,7,np.nan,np.nan,6,np.nan,np.nan])) == False
# assert ticTacToe.is_winning(np.array([1,np.nan,np.nan,np.nan,5,np.nan,np.nan,np.nan,9])) == True
# assert ticTacToe.is_winning(np.array([np.nan,np.nan,1,np.nan,5,np.nan,9,np.nan,np.nan])) == True
# assert ticTacToe.is_winning(np.array([1,np.nan,np.nan,np.nan,3,np.nan,np.nan,np.nan,9])) == False
# assert ticTacToe.is_winning(np.array([np.nan,np.nan,1,np.nan,3,np.nan,9,np.nan,np.nan])) == False
# assert ticTacToe.is_winning(np.array([9,6,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])) == False
# assert ticTacToe.is_winning(np.array([9,4,7,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])) == False
# assert ticTacToe.is_winning(np.array([9,2,4,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])) == True

# # test state_transition
# np.testing.assert_array_equal(ticTacToe.state_transition(np.array([1, 2, 3, 4, np.nan, np.nan, np.nan, np.nan, np.nan]), [7, 9]),
# np.array([1, 2, 3, 4, np.nan, np.nan, np.nan, 9, np.nan], dtype=float))

# # test step
# result = ticTacToe.step(np.array([1, 2, 3, 4, np.nan, np.nan, np.nan, np.nan, np.nan]), [7, 9])
# assert result[1] == -1
# assert result[2] == False

# result = ticTacToe.step(np.array([1, 5, np.nan, 4, np.nan, np.nan, np.nan, np.nan, np.nan]), [2, 9])
# assert result[1] == 10
# assert result[2] == True
