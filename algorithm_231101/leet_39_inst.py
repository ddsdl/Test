candidates = [2, 3, 6, 7]
target = 7

1. [2, 3, 6, 7]을 통해 반복
    [2]
    new_target = target - 2 = 5
    2. [2, 3, 6, 7]을 통해 반복
      [2]
      new_new_target = new_target - 2 = 3
        3. [2, 3, 6, 7]을 통해 반복
        [2]
         new_new_new_target = target - 2 = 1
        [3]
         new_new_new_target = target - 3 = 0
        [6, 7]
          음수가 나오면 더 이상 X
      [3]
      new_new_target = new_target - 3 = 2
      [6]
      new_new_target = new_target - 6 = -1 ===> 음수가 나오면 더 이상 X
      [7]
      new_new_target = new_target - 7 = -2 ===> 음수가 나오면 더이상 X
    [3]
    new_target = target - 3 = 4
    2. [2, 3, 6, 7]을 통해 반복
      [2]
      new_new_target = new_target - 2 = 2
      [3]
      new_new_target = new_target - 3 = 1
      
      


