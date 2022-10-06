package main

import "testing"

var kubus1 = Kubus{4}

func BenchmarkHitungLuas(b *testing.B) {
	for i := 0; i < b.N; i++ {
		kubus1.Luas()
	}
}
