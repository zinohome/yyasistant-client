from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.paramtype import PARAMTYPE
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParamDesc")


@_attrs_define
class ParamDesc:
    """
    Attributes:
        name (str):
        description (str):
        type_ (PARAMTYPE):
        required (bool):
        default (Union[bool, float, int, str]):
        range_ (Union[Unset, list[Union[float, int, str]]]):
        choices (Union[Unset, list[Union[float, int, str]]]):
    """

    name: str
    description: str
    type_: PARAMTYPE
    required: bool
    default: Union[bool, float, int, str]
    range_: Union[Unset, list[Union[float, int, str]]] = UNSET
    choices: Union[Unset, list[Union[float, int, str]]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        type_ = self.type_.value

        required = self.required

        default: Union[bool, float, int, str]
        default = self.default

        range_: Union[Unset, list[Union[float, int, str]]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = []
            for range_item_data in self.range_:
                range_item: Union[float, int, str]
                range_item = range_item_data
                range_.append(range_item)

        choices: Union[Unset, list[Union[float, int, str]]] = UNSET
        if not isinstance(self.choices, Unset):
            choices = []
            for choices_item_data in self.choices:
                choices_item: Union[float, int, str]
                choices_item = choices_item_data
                choices.append(choices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "type": type_,
                "required": required,
                "default": default,
            }
        )
        if range_ is not UNSET:
            field_dict["range"] = range_
        if choices is not UNSET:
            field_dict["choices"] = choices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        type_ = PARAMTYPE(d.pop("type"))

        required = d.pop("required")

        def _parse_default(data: object) -> Union[bool, float, int, str]:
            return cast(Union[bool, float, int, str], data)

        default = _parse_default(d.pop("default"))

        range_ = []
        _range_ = d.pop("range", UNSET)
        for range_item_data in _range_ or []:

            def _parse_range_item(data: object) -> Union[float, int, str]:
                return cast(Union[float, int, str], data)

            range_item = _parse_range_item(range_item_data)

            range_.append(range_item)

        choices = []
        _choices = d.pop("choices", UNSET)
        for choices_item_data in _choices or []:

            def _parse_choices_item(data: object) -> Union[float, int, str]:
                return cast(Union[float, int, str], data)

            choices_item = _parse_choices_item(choices_item_data)

            choices.append(choices_item)

        param_desc = cls(
            name=name,
            description=description,
            type_=type_,
            required=required,
            default=default,
            range_=range_,
            choices=choices,
        )

        param_desc.additional_properties = d
        return param_desc

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
