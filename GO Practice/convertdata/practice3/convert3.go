package main

import (
	"fmt"
	"strconv"
)

func main() {
	var str = "124"
	var num, err = strconv.ParseInt(str, 10, 64)

	if err == nil {
		fmt.Println(num)
	}
}
