from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_input_data import ConversationInputData


T = TypeVar("T", bound="ConversationInput")


@_attrs_define
class ConversationInput:
    """
    Attributes:
        data (Union[Unset, ConversationInputData]):
    """

    data: Union[Unset, "ConversationInputData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_input_data import ConversationInputData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, ConversationInputData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ConversationInputData.from_dict(_data)

        conversation_input = cls(
            data=data,
        )

        conversation_input.additional_properties = d
        return conversation_input

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
