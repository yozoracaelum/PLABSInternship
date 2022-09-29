package main

import (
	"fmt"
	"strconv"
)

func main() {
	var str = "24.12"
	var num, err = strconv.ParseFloat(str, 32)

	if err == nil {
		fmt.Println(num)
	}
}
