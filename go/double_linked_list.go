// I didn't write this go code, it's from [https://golang.org/pkg/container/list/](https://golang.org/pkg/container/list/) 
// I was going to write a doubly linked list, but go already implements it so well.

package main

import (
  "container/list"
  "fmt"
)

func main() {
  // Create a new list and put some numbers in it.
  l := list.New()
  e4 := l.PushBack(4)
  e1 := l.PushFront(1)
  l.InsertBefore(3, e4)
  l.InsertAfter(2, e1)

  // Iterate through list and print its contents.
  for e := l.Front(); e != nil; e = e.Next() {
    fmt.Println(e.Value)
  }
}

