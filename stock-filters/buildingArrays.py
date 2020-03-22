from random import choice

flours_6x6x3 = {
    "height": -1,
    "building": [[
    ["0:0", "2:0", "2:0", "2:0", "0:0", "2:0"],
    ["0:0", "0:0", "2:0", "2:0", "2:0", "2:0"],
    ["2:0", "2:0", "2:0", "2:0", "2:0", "0:0"],
    ["2:0", "2:0", "2:0", "2:0", "0:0", "2:0"],
    ["2:0", "2:0", "2:0", "2:0", "2:0", "0:0"],
    ["0:0", "2:0", "0:0", "2:0", "2:0", "2:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "96:6", "96:6", "0:0", "0:0"],
    ["0:0", "96:4", "2:0", "2:0", "68:0", "0:0"],
    ["0:0", "96:4", "2:0", "2:0", "96:5", "0:0"],
    ["0:0", "0:0", "96:7", "96:7", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [    
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "38:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
]]}

fountain_6x6x7 = {
    "height": -1,
    "building": [[
    ["3:0", "3:0", "3:0", "3:0", "3:0", "3:0"],
    ["3:0", "98:0", "98:0", "98:0", "98:0", "3:0"],
    ["3:0", "98:0", "9:0", "9:0", "98:0", "3:0"],
    ["3:0", "98:0", "9:0", "9:0", "98:0", "3:0"],
    ["3:0", "98:0", "98:0", "98:0", "98:0", "3:0"],
    ["3:0", "3:0", "3:0", "3:0", "3:0", "3:0"]
], [
    ["98:0", "98:0", "98:0", "98:0", "98:0", "98:0"],
    ["98:0", "98:0", "98:0", "98:0", "98:0", "98:0"],
    ["98:0", "98:0", "9:0", "9:0", "98:0", "98:0"],
    ["98:0", "98:0", "9:0", "9:0", "98:0", "98:0"],
    ["98:0", "98:0", "98:0", "98:0", "98:0", "98:0"],
    ["98:0", "98:0", "98:0", "98:0", "98:0", "98:0"]
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "98:0", "98:0", "98:0", "98:0", "0:0"],
    ["0:0", "98:0", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "98:0", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "98:0", "98:0", "98:0", "98:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "85:0", "0:0", "0:0", "85:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "85:0", "0:0", "0:0", "85:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "85:0", "0:0", "0:0", "85:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "85:0", "0:0", "0:0", "85:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "98:0", "98:0", "98:0", "98:0", "0:0"],
    ["0:0", "98:0", "98:0", "98:0", "98:0", "0:0"],
    ["0:0", "98:0", "98:0", "98:0", "98:0", "0:0"],
    ["0:0", "98:0", "98:0", "98:0", "98:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "50:5", "0:0", "0:0", "50:5", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "50:5", "0:0", "0:0", "50:5", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
]]}

house_8x8x7 = {
    "height": 0,
    "building": [[
    # first floor
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "17:0", "98:0", "98:0", "98:0", "98:0", "17:0", "0:0"],
    ["0:0", "98:0", "17:0", "5:0", "5:0", "17:0", "98:0", "0:0"],
    ["0:0", "98:0", "5:0", "5:0", "5:0", "5:0", "98:0", "0:0"],
    ["0:0", "98:0", "17:0", "5:0", "5:0", "17:0", "98:0", "0:0"],
    ["0:0", "17:0", "98:0", "98:0", "98:0", "98:0", "17:0", "0:0"],
    ["0:0", "0:0", "109:1", "109:1", "109:1", "109:1", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    # second floor
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "17:0", "98:0", "98:0", "98:0", "98:0", "17:0", "0:0"],
    ["0:0", "98:0", "53:3", "0:0", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "98:0", "26:13", "0:0", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "98:0", "26:1", "0:0", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "17:0", "98:0", "64:1", "64:2", "98:0", "17:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    # third floor
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "17:0", "17:8", "20:0", "20:0", "17:8", "17:0", "0:0"],
    ["0:0", "17:4", "0:0", "0:0", "0:0", "0:0", "17:4", "0:0"],
    ["0:0", "20:0", "0:0", "0:0", "0:0", "0:0", "20:0", "0:0"],
    ["0:0", "17:4", "0:0", "0:0", "0:0", "0:0", "17:4", "0:0"],
    ["0:0", "17:0", "17:8", "64:8", "64:8", "17:8", "17:0", "0:0"],
    ["0:0", "0:0", "50:1", "0:0", "0:0", "50:1", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    # fourth floor
    ["53:2", "53:11", "0:0", "0:0", "0:0", "0:0", "53:10", "53:3"],
    ["53:2", "17:0", "98:0", "98:0", "98:0", "98:0", "17:0", "53:3"],
    ["53:2", "98:0", "0:0", "0:0", "0:0", "0:0", "98:0", "53:3"],
    ["53:2", "98:0", "0:0", "0:0", "0:0", "0:0", "98:0", "53:3"],
    ["53:2", "98:0", "0:0", "50:2", "50:2", "0:0", "98:0", "53:3"],
    ["53:2", "17:0", "98:0", "98:0", "98:0", "98:0", "17:0", "53:3"],
    ["53:2", "53:11", "0:0", "0:0", "0:0", "0:0", "53:10", "53:3"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    # fifth floor
    ["0:0", "53:2", "53:11", "0:0", "0:0", "53:10", "53:3", "0:0"],
    ["0:0", "53:2", "98:0", "98:0", "98:0", "98:0", "53:3", "0:0"],
    ["0:0", "53:2", "0:0", "0:0", "0:0", "0:0", "53:3", "0:0"],
    ["0:0", "53:2", "0:0", "0:0", "0:0", "0:0", "53:3", "0:0"],
    ["0:0", "53:2", "0:0", "0:0", "0:0", "0:0", "53:3", "0:0"],
    ["0:0", "53:2", "98:0", "98:0", "98:0", "98:0", "53:3", "0:0"],
    ["0:0", "53:2", "53:11", "0:0", "0:0", "53:10", "53:3", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    # sixth floor
    ["0:0", "0:0", "53:2", "53:11", "53:10", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "98:0", "98:0", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "0:0", "0:0", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "0:0", "0:0", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "0:0", "0:0", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "98:0", "98:0", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "53:2", "53:11", "53:10", "53:3", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
], [
    # seventh floor
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "53:2", "53:3", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"]
]]}

farm_10x10x2 = {
    "height": -1,
    "building": [[
    ["17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0"],
    ["17:0", "60:0", "9:0", "60:0", "60:0", "60:0", "60:0", "9:0", "60:0", "17:0"],
    ["17:0", "60:0", "9:0", "60:0", "60:0", "60:0", "60:0", "9:0", "60:0", "17:0"],
    ["17:0", "60:0", "9:0", "60:0", "60:0", "60:0", "60:0", "9:0", "60:0", "17:0"],
    ["17:0", "60:0", "9:0", "60:0", "60:0", "60:0", "60:0", "9:0", "60:0", "17:0"],
    ["17:0", "60:0", "9:0", "60:0", "60:0", "60:0", "60:0", "9:0", "60:0", "17:0"],
    ["17:0", "60:0", "9:0", "60:0", "60:0", "60:0", "60:0", "9:0", "60:0", "17:0"],
    ["17:0", "60:0", "9:0", "60:0", "60:0", "60:0", "60:0", "9:0", "60:0", "17:0"],
    ["17:0", "60:0", "9:0", "60:0", "60:0", "60:0", "60:0", "9:0", "60:0", "17:0"],
    ["17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "141:7", "0:0", "59:7", "59:7", "59:7", "59:7", "0:0", "142:7", "0:0"],
    ["0:0", "141:7", "0:0", "59:7", "59:7", "59:7", "59:7", "0:0", "142:7", "0:0"],
    ["0:0", "141:7", "0:0", "59:7", "59:7", "59:7", "59:7", "0:0", "142:7", "0:0"],
    ["0:0", "141:7", "0:0", "59:7", "59:7", "59:7", "59:7", "0:0", "142:7", "0:0"],
    ["0:0", "141:7", "0:0", "59:7", "59:7", "59:7", "59:7", "0:0", "142:7", "0:0"],
    ["0:0", "141:7", "0:0", "59:7", "59:7", "59:7", "59:7", "0:0", "142:7", "0:0"],
    ["0:0", "141:7", "0:0", "59:7", "59:7", "59:7", "59:7", "0:0", "142:7", "0:0"],
    ["0:0", "141:7", "0:0", "59:7", "59:7", "59:7", "59:7", "0:0", "142:7", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],

]]}

tree_10x10x9 = {
    "height": -1,
    "building": [[
    ["0:0", "0:0", "13:0", "0:0", "208:0", "13:0", "0:0", "208:0", "0:0", "0:0"],
    ["208:0", "0:0", "208:0", "13:0", "13:0", "208:0", "13:0", "0:0", "208:0", "13:0"],
    ["208:0", "13:0", "208:0", "3:0", "3:0", "3:0", "0:0", "13:0", "0:0", "208:0"],
    ["0:0", "208:0", "13:0", "3:0", "208:0", "3:0", "0:0", "208:0", "0:0", "0:0"],
    ["0:0", "0:0", "13:0", "3:0", "3:0", "3:0", "208:0", "208:0", "0:0", "13:0"],
    ["208:0", "13:0", "208:0", "208:0", "13:0", "208:0", "208:0", "13:0", "0:0", "208:0"],
    ["13:0", "208:0", "13:0", "0:0", "208:0", "13:0", "13:0", "208:0", "13:0", "0:0"],
    ["0:0", "208:0", "0:0", "13:0", "13:0", "208:0", "13:0", "13:0", "0:0", "208:0"],
    ["208:0", "0:0", "208:0", "208:0", "208:0", "0:0", "13:0", "0:0", "13:0", "208:0"],
    ["13:0", "208:0", "13:0", "0:0", "0:0", "13:0", "0:0", "13:0", "208:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "31:2", "0:0", "0:0", "0:0", "0:0", "85:0", "0:0"],
    ["0:0", "85:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "109:0", "109:0", "109:0", "31:2", "0:0", "31:2", "0:0"],
    ["0:0", "0:0", "0:0", "109:2", "17:0", "109:3", "31:2", "0:0", "0:0", "0:0"],
    ["0:0", "31:2", "0:0", "109:1", "109:1", "109:1", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "31:2", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["31:2", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "85:0", "0:0"],
    ["0:0", "31:2", "0:0", "0:0", "0:0", "31:2", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "38:5", "85:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "17:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "50:2", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "50:4", "17:0", "50:3", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "50:1", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "17:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "18:0", "18:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "18:0", "18:0", "18:0", "18:0", "18:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "18:0", "18:0", "17:0", "18:0", "18:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "18:0", "18:0", "18:0", "18:0", "18:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "18:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "18:0", "18:0", "18:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "18:0", "18:0", "18:0", "18:0", "18:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "18:0", "18:0", "17:0", "18:0", "18:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "18:0", "18:0", "18:0", "18:0", "18:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "18:0", "0:0", "18:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "18:0", "18:0", "18:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "18:0", "17:0", "18:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "18:0", "18:0", "18:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "18:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "18:0", "18:0", "18:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "18:0", "18:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
]]}

mansion_12x12x11 = {
    "height": -1,
    "building": [[
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "3:0", "3:0", "3:0", "3:0", "3:0", "3:0", "3:0", "3:0", "3:0", "0:0"],
    ["0:0", "0:0", "3:0", "98:0", "98:0", "98:0", "98:0", "98:0", "98:0", "98:0", "3:0", "0:0"],
    ["0:0", "0:0", "3:0", "98:0", "98:0", "98:0", "98:0", "98:0", "98:0", "98:0", "3:0", "0:0"],
    ["0:0", "0:0", "3:0", "98:0", "98:0", "98:0", "98:0", "98:0", "98:0", "98:0", "3:0", "0:0"],
    ["0:0", "0:0", "3:0", "3:0", "3:0", "3:0", "98:0", "3:0", "3:0", "3:0", "3:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "17:0", "98:0", "98:0", "98:0", "17:0", "98:0", "98:0", "98:0", "17:0", "0:0"],
    ["0:0", "0:0", "98:0", "0:0", "0:0", "98:0", "98:0", "109:3", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "0:0", "98:0", "26:13", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "0:0", "98:0", "26:1", "0:0", "0:0", "0:0", "0:0", "26:0", "26:8", "98:0", "0:0"],
    ["0:0", "0:0", "17:0", "98:0", "98:0", "98:0", "64:2", "98:0", "98:0", "98:0", "17:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "17:0", "98:0", "20:0", "98:0", "17:0", "98:0", "20:0", "98:0", "17:0", "0:0"],
    ["0:0", "0:0", "98:0", "0:0", "0:0", "98:0", "109:3", "0:0", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "0:0", "20:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "20:0", "0:0"],
    ["0:0", "0:0", "98:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "0:0", "17:0", "98:0", "20:0", "98:0", "64:8", "98:0", "20:0", "98:0", "17:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "17:0", "98:0", "98:0", "98:0", "17:0", "98:0", "98:0", "98:0", "17:0", "0:0"],
    ["0:0", "0:0", "98:0", "98:0", "98:0", "109:3", "0:0", "0:0", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "0:0", "98:0", "50:3", "0:0", "0:0", "0:0", "0:0", "0:0", "50:4", "98:0", "0:0"],
    ["0:0", "0:0", "98:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "98:0", "0:0"],
    ["0:0", "0:0", "17:0", "98:0", "98:0", "98:0", "98:0", "98:0", "98:0", "98:0", "17:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "17:0", "0:0"],
    ["0:0", "0:0", "17:0", "98:0", "109:3", "0:0", "0:0", "0:0", "5:0", "5:0", "17:4", "0:0"],
    ["0:0", "0:0", "17:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "17:4", "0:0"],
    ["0:0", "0:0", "17:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "17:4", "0:0"],
    ["0:0", "0:0", "17:0", "17:8", "17:8", "17:8", "17:0", "17:8", "17:8", "17:8", "17:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "17:0", "5:0", "5:0", "5:0", "17:0", "5:0", "5:0", "5:0", "17:0", "0:0"],
    ["0:0", "0:0", "5:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "5:0", "0:0"],
    ["0:0", "0:0", "5:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "5:0", "0:0"],
    ["0:0", "0:0", "5:0", "26:10", "26:2", "0:0", "0:0", "0:0", "26:0", "26:8", "5:0", "0:0"],
    ["0:0", "0:0", "17:0", "5:0", "5:0", "5:0", "17:0", "5:0", "5:0", "5:0", "17:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "17:0", "5:0", "20:0", "5:0", "17:0", "5:0", "20:0", "5:0", "17:0", "0:0"],
    ["0:0", "0:0", "5:0", "0:0", "0:0", "0:0", "50:1", "0:0", "0:0", "0:0", "5:0", "0:0"],
    ["0:0", "0:0", "20:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "20:0", "0:0"],
    ["0:0", "0:0", "5:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "5:0", "0:0"],
    ["0:0", "0:0", "17:0", "5:0", "20:0", "5:0", "17:0", "5:0", "20:0", "5:0", "17:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
], [
    ["0:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0"],
    ["0:0", "0:0", "17:0", "5:0", "5:0", "5:0", "17:0", "5:0", "5:0", "5:0", "17:0", "0:0"],
    ["0:0", "0:0", "5:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "5:0", "0:0"],
    ["0:0", "0:0", "5:0", "50:3", "0:0", "0:0", "0:0", "0:0", "0:0", "50:4", "5:0", "0:0"],
    ["0:0", "0:0", "5:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "5:0", "0:0"],
    ["0:0", "0:0", "17:0", "5:0", "5:0", "5:0", "17:0", "5:0", "5:0", "5:0", "17:0", "0:0"],
    ["0:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],

], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0"],
    ["0:0", "0:0", "5:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "5:0", "0:0"],
    ["0:0", "0:0", "5:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "5:0", "0:0"],
    ["0:0", "0:0", "5:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "5:0", "0:0"],
    ["0:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],

], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0"],
    ["0:0", "0:0", "5:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "5:0", "0:0"],
    ["0:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],

], [
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0", "5:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],
    ["0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0", "0:0"],

]]}

class BuildingFactory():
    def __init__(self):
        self.buildings = {
            6: [flours_6x6x3, fountain_6x6x7],
            8: [house_8x8x7],
            10: [farm_10x10x2, tree_10x10x9],
            12: [mansion_12x12x11]
        }

    def choose_building(self, width):
        try:
            return choice(self.buildings[width])
        except:
            return None
