/**
 * Created by Ashish Patel
 * Copyright © 2017 ashish.me
 * ashishsushilpatel@gmail.com 
 */

/**
 * Program:
 * Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array.
 * For example, ["hello", "Hello"], should return true because all of the letters in the second string are present in the first, ignoring case.
 * The arguments ["hello", "hey"] should return false because the string "hello" does not contain a "y".
 * Lastly, ["Alien", "line"], should return true because all of the letters in "line" are present in "Alien".
 */

function mutation(arr)
 {
    if(arr[0].length <= arr[1].length){
      str1 = arr[0].split('');
      str2 = arr[1].split('');
      str1.forEach(element => {
        console.log(element);
      });
      console.log(str1);
      console.log(str2);
    }else{
      str1 = arr[0].split('');
      str2 = arr[1].split('');
      console.log(str1);
      console.log(str2);
      str2.forEach(element => {
        console.log(str1.indexOf(element));
      });
    }
    return arr[0].lowercase == arr[1].lowercase;
  }
  
console.log(mutation(["floor", "for"]));