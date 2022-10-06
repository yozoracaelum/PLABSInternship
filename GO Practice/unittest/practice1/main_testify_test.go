package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

var (
	kubus2              Kubus   = Kubus{4}
	volumeSeharusnya2   float64 = 64
	luasSeharusnya2     float64 = 96
	kelilingSeharusnya2 float64 = 48
)

func TestHitungVolume2(t *testing.T) {
	assert.Equal(t, kubus2.Volume(), volumeSeharusnya2, "perhitungan volume salah")
}

func TestHitungLuas2(t *testing.T){
	assert.Equal(t, kubus2.Luas(), luasSeharusnya2, "perhitungan luas salah")
}

func TestHitungKeliling2(t *testing.T){
	assert.Equal(t, kubus2.Keliling(), kelilingSeharusnya2, "perhitungan keliling salah" )
}
