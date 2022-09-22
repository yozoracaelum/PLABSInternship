package main

import "fmt"

func main() {
	s := []int{1, 2, 4, 6, 8}
	//1,2,2,3,8
	s[2] = s[1]
	s[3] = s[2] + s[0]
	fmt.Println(s[4] % s[3])
}
