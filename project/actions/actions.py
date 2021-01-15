from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database_connection import dataUpdate


class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Calls dataUpdate function from database_connection.py and sends the slots values it collected from chatbot
        dataUpdate(tracker.get_slot("name"),tracker.get_slot("address"),tracker.get_slot("zipcode"),tracker.get_slot("mobile"),tracker.get_slot("items"))

        return []
