-- let p = putStrLn string

main :: IO ()
main = do
  let
    visited = []
    string = "^>v<^^>"

    pr char
        | char == "^" = putStrLn n
        | char == "v" = putStrLn s
        | char == ">" = putStrLn e
        | char == "<" = putStrLn w
        | otherwise = putStrLn ("What? " ++ char ++ "?")
        where
          n = "north"
          s = "south"
          w = "east"
          e = "west"

  mapM pr string


  putStrLn string
  putStrLn "Hello World!"
