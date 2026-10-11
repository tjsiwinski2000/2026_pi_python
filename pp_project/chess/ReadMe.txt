1002-2026
- issue with some piece images
The images were missing because chessboard.js defaults to searching for image files on your local server relative path (img/chesspieces/wikipedia/{piece}.png). When hosted strictly inside a single file without downloading local assets, those image calls fail.
- otherwise seems decent all-in-one chess file solution