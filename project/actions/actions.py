# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database_connection import dataUpdate

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit_request"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(text="Your Name is {0}\n and your address is {1}\n your phone number is {2}\n your requested items are {3}\n".format(tracker.get_slot("name"),tracker.get_slot("address"),tracker.get_slot("mobile"),tracker.get_slot("items")))
        dataUpdate(tracker.get_slot("name"),tracker.get_slot("address"),tracker.get_slot("zipcode"),tracker.get_slot("mobile"),tracker.get_slot("items"))

        return []
