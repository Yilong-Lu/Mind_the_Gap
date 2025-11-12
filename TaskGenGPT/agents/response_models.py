from pydantic import BaseModel, Field, constr
from typing import List

class RequiredItem(BaseModel):
    """
    Model representing an item required for the task, including its quantity.
    """
    name: str = Field(
        ...,
        description="The name of the required item, selected from the predefined item list."
    )
    quantity: int = Field(
        ...,
        description="The quantity of the required item. Must be a positive integer."
    )

class RequiredItems(BaseModel):
    items: List[RequiredItem] = Field(
        ...,
        description="List of required items"
    )

class TaskReport(BaseModel):
    """
    Model representing a task report interface.
    """
    
    task_name: str = Field(
        ...,
        description=(
            "A short name for the task. "
            "The task name should be fewer than 6 words."
        )
    )
    
    required_items: List[RequiredItem] = Field(
        ...,
        description=(
            "List of necessary items selected from the predefined item list. "
            "Select all items that are required for the task."
        )
    )
    
    task_description: str = Field(
        ...,
        description=(
            "Briefly describe the task. "
            'Placeholder text: "In this task, the player..."'
        )
    )
    
    detailed_task_setup: str = Field(
        ...,
        description=(
            "Describe how the items are arranged and interacted with in the task. "
            'Placeholder text: "To start this task, the player needs..."'
        )
    )
    
    task_goal: str = Field(
        ...,
        description=(
            "Describe the goal of the task. "
            'Placeholder text: "The goal of this task is..."'
        )
    )
    
    scoring_system: str = Field(
        ...,
        description=(
            "Describe the scoring method. "
            'Placeholder text: "In this task..."'
        )
    )


class TasksReport(BaseModel):
    """
    Model representing the tasks report interface.
    """
    tasks: List[TaskReport] = Field(..., description="List of tasks report")


class ItemUsageAnalysis(BaseModel):
    """
    Model representing the analysis of an item's typical usage versus its task-specific usage.
    """
    item_name: str = Field(
        ...,
        description="The name of the item being analyzed"
    )
    typical_usage: str = Field(
        ...,
        description="The common or conventional usage of this item in everyday scenarios"
    )
    task_specific_usage: str = Field(
        ...,
        description="How this item is specifically used in the current task"
    )
    usage_alignment: int = Field(
        ...,
        ge=1,
        le=5,
        description=(
            "A score from 1-5 indicating how typical the task-specific usage is compared to conventional usage. "
            "1: Extremely unconventional usage, "
            "2: Unconventional usage, "
            "3: Neutral usage, "
            "4: Conventional usage, "
            "5: Extremely conventional usage"
        )
    )

class ItemAffordanceAnalysis(BaseModel):
    """
    Model representing the analysis of an item's typical affordances versus its task-specific affordances.
    """
    item_name: str = Field(
        ...,
        description="The name of the item being analyzed"
    )
    typical_affordance: str = Field(
        ...,
        description="The item's typical one or more typical affordances"
    )
    task_specific_affordance: str = Field(
        ...,
        description="The item's specific affordance in the current task"
    )
    affordance_alignment: int = Field(
        ...,
        ge=1,
        le=5,
        description=(
            "A score from 1-5 indicating how typical the task-specific affordance is compared to the item's typical affordances. "
            "1: Extremely unconventional affordance, "
            "2: Unconventional affordance, "
            "3: Neutral affordance, "
            "4: Conventional affordance, "
            "5: Extremely conventional affordance"
        )
    )

class ItemsUsageReport(BaseModel):
    """
    Model representing the report of the analysis of items' typical usage versus their task-specific usage.
    """
    items: List[ItemUsageAnalysis] = Field(..., description="List of items and their usage analysis" )

class ItemsAffordanceReport(BaseModel):
    """
    Model representing the report of the analysis of items' typical affordances versus their task-specific affordances.
    """
    items: List[ItemAffordanceAnalysis] = Field(..., description="List of items and their affordances analysis" )

class SingleItemUsageReport(BaseModel):
    """
    Model representing the report of the analysis of a single item's usage.
    """
    item_name: str = Field(
        ...,
        description="The name of the item being analyzed"
    )
    typical_usage_description: str = Field(
        ...,
        description="A description of the item's typical usage"
    )
    typical_usage_phrase: str = Field(
        ...,
        description="A phrase describing the item's typical usage"
    )
    typical_affordances: List[str] = Field(
        ...,
        description="The item's typical one or more affordances"
    )
    

class SingleItemUsageReports(BaseModel):
    """
    Model representing the report of the analysis of multiple items' usage.
    """
    items: List[SingleItemUsageReport] = Field(..., description="List of items and their usage/affordances analysis")

