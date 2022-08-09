from tkinter.messagebox import NO
from typing import Any, Text, Dict, List
from urllib import response

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.types import DomainDict
from rasa_sdk.events import UserUtteranceReverted, EventType

import re
from . import validation


class ActionTofallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        dispatcher.utter_message(response="utter_please_rephrase")
        return [UserUtteranceReverted()]


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_greet")

        return []


class ValidatePersonalDetailsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_survey"
    

    def validate_recommend(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if validation.choices(slot_value, 3):
            return {"recommend": slot_value}
        else:
            dispatcher.utter_message(text="Invalid input, please enter a valid input")
            return {"recommend": None}
    
    def validate_management(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if validation.agree_status(slot_value):
            return {"management": slot_value}
        else:
            dispatcher.utter_message(text="Invalid input, please enter a valid input")
            return {"management": None}

    def validate_strategy(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if validation.agree_status(slot_value):
            return {"strategy": slot_value}
        else:
            dispatcher.utter_message(text="Invalid input, please enter a valid input")
            return {"strategy": None}

    def validate_development(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if validation.agree_status(slot_value):
            return {"development": slot_value}
        else:
            dispatcher.utter_message(text="Invalid input, please enter a valid input")
            return {"development": None}

    def validate_mistakes(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if validation.agree_status(slot_value):
            return {"mistakes": slot_value}
        else:
            dispatcher.utter_message(text="Invalid input, please enter a valid input")
            return {"mistakes": None}

    def validate_daily_problems(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if validation.agree_status(slot_value):
            return {"daily_problems": slot_value}
        else:
            dispatcher.utter_message(text="Invalid input, please enter a valid input")
            return {"daily_problems": None}

    def validate_treat(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if validation.agree_status(slot_value):
            return {"treat": slot_value}
        else:
            dispatcher.utter_message(text="Invalid input, please enter a valid input")
            return {"treat": None}
    
    def validate_satisfied(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if validation.choices(slot_value, 5):
            return {"satisfied": slot_value}
        else:
            dispatcher.utter_message(text="Invalid input, please enter a valid input")
            return {"satisfied": None}
    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        if (re.search(regex, slot_value)):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text="Invalid email, please enter a valid email")
            return {"email": None}