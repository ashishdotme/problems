/**
 * Created by Ashish Patel
 * Copyright © 2018 ashish.me
 * ashishsushilpatel@gmail.com
 */

function frankenSplice(arr1, arr2, n) {
  let newArr = [...arr2];
  newArr.splice(n,0,...arr1)
  return newArr;
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);