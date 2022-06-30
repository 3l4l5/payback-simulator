# payback-simulator

## 各キーの意味
```
{
    "単勝": "win",
    "複勝": "place",
    "三連単": "trifecta",
    "三連複": "triple",
    "ワイド": "wide",
    "馬単": "quinella",
    "馬連": "extra",
    "枠連": "braket",
}
```

## payback json のフォーマット

```json
{
    <race_id>:{
        "win":{
            "horse":<horse_num>,
            "payback":<payback refund>
        },
        "place":{
            ...
        },
        ...
        "triple":{
            "horse":[<horse>,<horse>,<horse>],
            "payback":<payback refund>
        }
    },
    ...
}
```

### example
```
{
    "201804030309": {
        "win": {
            "horse": 2,
            "payback": 1880
        },
        "place": {
            "horse": [
                2,
                11,
                3
            ],
            "payback": [
                540,
                350,
                200
            ]
        },
        "braket": {
            "horse": [
                2,
                8
            ],
            "payback": 5920
        },
        "extra": {
            "horse": [
                2,
                11
            ],
            "payback": 8390
        },
        "wide": {
            "horse": [
                [
                    2,
                    11
                ],
                [
                    2,
                    3
                ],
                [
                    3,
                    11
                ]
            ],
            "payback": [
                2270,
                970,
                780
            ]
        },
        "quinella": {
            "horse": [
                2,
                11
            ],
            "payback": 19580
        },
        "triple": {
            "horse": [
                2,
                3,
                11
            ],
            "win_prize": 12600
        },
        "trifecta": {
            "horse": [
                2,
                11,
                3
            ],
            "win_prize": 117410
        }
    },
```

## buy tableのフォーマット


```json
{
    <race_id>:{
        "win":[
            {"horse":<horse>, "num": <num of ticket>},
            {"horse":<horse>, "num": <num of ticket>},
            {"horse":<horse>, "num": <num of ticket>},
            ...
            ],
        "place":[
            {"horse":<horse>, "num": <num of ticket>},
            {"horse":<horse>, "num": <num of ticket>},
            {"horse":<horse>, "num": <num of ticket>},
            ...
            ],
        ...
        "triple":[
            {"horse":[<horse>, <horse>, <horse>], "num":<num of ticket>},
            {"horse":[<horse>, <horse>, <horse>], "num":<num of ticket>},
            {"horse":[<horse>, <horse>, <horse>], "num":<num of ticket>},
            ...
        ]
    }
}

```

## return body の形式

```json
{
    "summary":{
        "return_amount": <yen>,
        "purchase_cost":<yen>
    },
    "betting_ticket_on_the_mark":{
        <race_id>: {
            "win":{
                "horse":<horse_num>,
                "payback":<payback refund>,
                "num":<num of ticket>
            },
            "place":{...},
            ...
        }
        ...
    }
}
```