# RuleUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**list[RuleActionUpdate]**](RuleActionUpdate.md) |  | 
**active** | **bool** | Whether or not the rule is even active. Default is true. | [optional] 
**description** | **str** |  | [optional] 
**rule_group_id** | **int** | ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory. | 
**rule_group_title** | **str** | Title of the rule group under which the rule must be stored. Either this field or rule_group_id is mandatory. | [optional] 
**stop_processing** | **bool** | If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false. | [optional] 
**strict** | **bool** | If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true. | [optional] 
**title** | **str** |  | 
**trigger** | **str** | Which action is necessary for the rule to fire? Use either store-journal or update-journal. | 
**triggers** | [**list[RuleTriggerUpdate]**](RuleTriggerUpdate.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


