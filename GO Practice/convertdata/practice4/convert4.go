package main

import (
	"fmt"
	"strconv"
)

func main() {
	var str = "1010"
	var num, err = strconv.ParseInt(str, 2, 8)

	if err == nil {
		fmt.Println(num)
	}
}
