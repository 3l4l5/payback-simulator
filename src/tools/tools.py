import os
import json

MOUNT_POINT = os.environ["MOUNT_POINT"]


def check_json_type(posted_dict :dict) -> bool:
    return True

def calk_win_payback(win_horse_actual: dict, win_horse_predict: list) -> dict:
    total_buy_ticket = 0
    payback = 0
    result_dict_list = []
    for buy_dict in win_horse_predict:
        total_buy_ticket += buy_dict["amount"]
        if buy_dict["horse"] == win_horse_actual["horse"]:
            payback = buy_dict["amount"] * win_horse_actual["payback"]
            result_dict = buy_dict
            result_dict["payback"] = payback
            result_dict_list.append(result_dict)
        else:
            result_dict = buy_dict
            result_dict["payback"] = 0
            result_dict_list.append(result_dict)
    total_cost = total_buy_ticket * 100
    profit = payback - total_cost
    return {
        "return_amount": profit,
        "purchase_cost": total_cost,
        "results": result_dict_list
    }

def calk_payback(posted_json: dict) -> dict:
    """calk payback dict.

    Args:
        posted_json (dict): posted dict witch we want to simulate.

    Returns:
        dict: _description_
    """
    with open(os.path.join(MOUNT_POINT, "all_payback.json")) as json_file_object:
        payback_json = json.load(json_file_object)
    result_dict = {}
    ticket_cost = 0
    payback_sum = 0
    for race_id in posted_json:
        result_dict[race_id] = {}
        payback_result = payback_json[race_id]
        buy_ticket = posted_json[race_id]

        # NOTE: Buy ticket's shape ↓
        # buy_ticket = {
        #     "win": "~~~",
        #     "place": "~~~",
        #     "triple": "~~~",
        #     "~~~" : "~~~"
        # }
        for ticket_type in buy_ticket:
            if ticket_type == "win":
                win_results = payback_result["win"]
                win_horses_predict = buy_ticket["win"]
                # NOTE: win_results shape
                # win_results = {"horse": "~~~", "payback": "~~~"}
                # NOTE: win_horses_predict shape
                # win_horses_predict = [
                #     {"horse":<horse>, "amount": <num of ticket>},
                #     {"horse":<horse>, "amount": <num of ticket>},
                #     {"horse":<horse>, "amount": <num of ticket>},
                # ]
                win_payback_result = calk_win_payback(
                                            win_horse_actual=win_results,
                                            win_horse_predict=win_horses_predict
                                            )
                payback_sum += win_payback_result["return_amount"]
                ticket_cost += win_payback_result["purchase_cost"]
                result_dict[race_id]["win"] = win_payback_result["results"]

            elif ticket_type == "place":
                pass

            elif ticket_type == "trifecta":
                pass

            elif ticket_type == "triple":
                pass

            elif ticket_type == "wide":
                pass

            elif ticket_type == "quinella":
                pass

            elif ticket_type == "extra":
                pass

            elif ticket_type == "braket":
                pass

    return {
        "summary": {
            "return_amount": payback_sum,
            "purchase_count": ticket_cost
        },
        "betting_ticket_on_the_mark": result_dict
    }

if __name__ == "__main__":
    posted_json = {
        "201804030309": {
            "win": [
                {"horse":1, "amount": 100},
                {"horse":2, "amount": 100},
                {"horse":3, "amount": 100},
            ],
            "place": [
                {"horse":1, "amount": 100},
                {"horse":2, "amount": 100},
                {"horse":3, "amount": 100},
            ],
            "triple": [
                {"horse":[1,2,3], "amount": 100},
                {"horse":[4,3,5], "amount": 100},
                {"horse":[4,3,1], "amount": 100},
            ]
        },
    }
    print(calk_payback(posted_json))