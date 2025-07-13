from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.responsecode import RESPONSECODE

T = TypeVar("T", bound="ASREngineOutput")


@_attrs_define
class ASREngineOutput:
    """
    Attributes:
        code (RESPONSECODE):
        message (str):
        data (str):
    """

    code: RESPONSECODE
    message: str
    data: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = RESPONSECODE(d.pop("code"))

        message = d.pop("message")

        data = d.pop("data")

        asr_engine_output = cls(
            code=code,
            message=message,
            data=data,
        )

        asr_engine_output.additional_properties = d
        return asr_engine_output

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
