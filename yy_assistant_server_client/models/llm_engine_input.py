from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.llm_engine_input_config import LLMEngineInputConfig


T = TypeVar("T", bound="LLMEngineInput")


@_attrs_define
class LLMEngineInput:
    """
    Attributes:
        engine (Union[Unset, str]):  Default: 'default'.
        config (Union[Unset, LLMEngineInputConfig]):
        data (Union[File, Unset, str]):  Default: ''.
    """

    engine: Union[Unset, str] = "default"
    config: Union[Unset, "LLMEngineInputConfig"] = UNSET
    data: Union[File, Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        engine = self.engine

        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        data: Union[FileTypes, Unset, str]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, File):
            data = self.data.to_tuple()

        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if engine is not UNSET:
            field_dict["engine"] = engine
        if config is not UNSET:
            field_dict["config"] = config
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.llm_engine_input_config import LLMEngineInputConfig

        d = dict(src_dict)
        engine = d.pop("engine", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, LLMEngineInputConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = LLMEngineInputConfig.from_dict(_config)

        def _parse_data(data: object) -> Union[File, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                data_type_1 = File(payload=BytesIO(data))

                return data_type_1
            except:  # noqa: E722
                pass
            return cast(Union[File, Unset, str], data)

        data = _parse_data(d.pop("data", UNSET))

        llm_engine_input = cls(
            engine=engine,
            config=config,
            data=data,
        )

        llm_engine_input.additional_properties = d
        return llm_engine_input

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
