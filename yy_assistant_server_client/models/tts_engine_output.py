from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audiotype import AUDIOTYPE
from ..models.responsecode import RESPONSECODE
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="TTSEngineOutput")


@_attrs_define
class TTSEngineOutput:
    """
    Attributes:
        code (RESPONSECODE):
        message (str):
        data (Union[File, None, Unset, str]):
        type_ (Union[Unset, AUDIOTYPE]):
        sample_rate (Union[Unset, int]):  Default: 16000.
        sample_width (Union[Unset, int]):  Default: 2.
    """

    code: RESPONSECODE
    message: str
    data: Union[File, None, Unset, str] = UNSET
    type_: Union[Unset, AUDIOTYPE] = UNSET
    sample_rate: Union[Unset, int] = 16000
    sample_width: Union[Unset, int] = 2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        data: Union[FileTypes, None, Unset, str]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, File):
            data = self.data.to_tuple()

        else:
            data = self.data

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        sample_rate = self.sample_rate

        sample_width = self.sample_width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sample_rate is not UNSET:
            field_dict["sampleRate"] = sample_rate
        if sample_width is not UNSET:
            field_dict["sampleWidth"] = sample_width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = RESPONSECODE(d.pop("code"))

        message = d.pop("message")

        def _parse_data(data: object) -> Union[File, None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                data_type_1 = File(payload=BytesIO(data))

                return data_type_1
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset, str], data)

        data = _parse_data(d.pop("data", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AUDIOTYPE]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AUDIOTYPE(_type_)

        sample_rate = d.pop("sampleRate", UNSET)

        sample_width = d.pop("sampleWidth", UNSET)

        tts_engine_output = cls(
            code=code,
            message=message,
            data=data,
            type_=type_,
            sample_rate=sample_rate,
            sample_width=sample_width,
        )

        tts_engine_output.additional_properties = d
        return tts_engine_output

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
