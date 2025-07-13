from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.audiotype import AUDIOTYPE
from ..types import File

T = TypeVar("T", bound="BodyApiAsrInferFileYyhAsrV0EngineFilePost")


@_attrs_define
class BodyApiAsrInferFileYyhAsrV0EngineFilePost:
    """
    Attributes:
        file (File):
        engine (str):
        type_ (AUDIOTYPE):
        config (str):
        sample_rate (int):
        sample_width (int):
    """

    file: File
    engine: str
    type_: AUDIOTYPE
    config: str
    sample_rate: int
    sample_width: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        engine = self.engine

        type_ = self.type_.value

        config = self.config

        sample_rate = self.sample_rate

        sample_width = self.sample_width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "engine": engine,
                "type": type_,
                "config": config,
                "sampleRate": sample_rate,
                "sampleWidth": sample_width,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        files.append(("engine", (None, str(self.engine).encode(), "text/plain")))

        files.append(("type", (None, str(self.type_.value).encode(), "text/plain")))

        files.append(("config", (None, str(self.config).encode(), "text/plain")))

        files.append(("sampleRate", (None, str(self.sample_rate).encode(), "text/plain")))

        files.append(("sampleWidth", (None, str(self.sample_width).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        engine = d.pop("engine")

        type_ = AUDIOTYPE(d.pop("type"))

        config = d.pop("config")

        sample_rate = d.pop("sampleRate")

        sample_width = d.pop("sampleWidth")

        body_api_asr_infer_file_yyh_asr_v0_engine_file_post = cls(
            file=file,
            engine=engine,
            type_=type_,
            config=config,
            sample_rate=sample_rate,
            sample_width=sample_width,
        )

        body_api_asr_infer_file_yyh_asr_v0_engine_file_post.additional_properties = d
        return body_api_asr_infer_file_yyh_asr_v0_engine_file_post

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
