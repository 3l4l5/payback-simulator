# payback-simulator

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