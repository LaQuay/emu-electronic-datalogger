# emu-electronic-datalogger

Unofficial parser for Emu Electronic AG datalogger. Tested using a Water sensor manufactured by APA (v21).

*Disclaimer: This is an educational code made for testing purposes. Use at your own risk.*

## Setup & Run

### How to obtain the input data

1. Access your emu datalogger via the website
2. Go to "System Integration"
3. Select your "From" and "To" date
4. Select "Water meter": `Medium`
5. Select "Export-Type": `json`
6. Select "Filter": `per month`
7. CLick Export

The export operation takes some time. For example, for 10 flats, 6 months it takes around 10 minutes.

### Once you have your input data

1. Place it in the `./in` folder
2. Write your desired filename
3. Write your desired header

### Result

There will be a single `.csv` file in the `./out` folder.

## Notes

This example assumes (in `get_flat_door_from_filename`) the name of each device starts with `PL`. You might need
to do some adaptations.

## Example

This is what the output file `./out/FILENAME.csv` will look like once the code is executed, this is a summary for flats 5A to 5G.

```csv
Hoja de consumos de agua caliente por piso - HEADER
Piso;Diferencia de consumo (m3);2023-09-30;2023-10-31;2023-11-30;2023-12-31;2024-01-25
05A;22,123;132,245;137,791;142,368;148,756;154,368
05B;9,925;58,974;60,973;63,573;66,603;68,899
05C;2,186;27,799;28,255;28,759;29,568;29,985
05D;0,341;9,469;9,476;9,574;9,702;9,81
05E;8,478;48,683;50,949;53,807;55,057;57,161
05G;3,967;31,701;32,629;34,015;34,826;35,668
```
