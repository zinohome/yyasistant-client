from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enginetype import ENGINETYPE
from ..models.infertype import INFERTYPE
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_desc_meta import EngineDescMeta


T = TypeVar("T", bound="EngineDesc")


@_attrs_define
class EngineDesc:
    """
    Attributes:
        name (str):
        type_ (ENGINETYPE):
        infer_type (INFERTYPE):
        desc (Union[Unset, str]):  Default: ''.
        meta (Union[Unset, EngineDescMeta]):
    """

    name: str
    type_: ENGINETYPE
    infer_type: INFERTYPE
    desc: Union[Unset, str] = ""
    meta: Union[Unset, "EngineDescMeta"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        infer_type = self.infer_type.value

        desc = self.desc

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "infer_type": infer_type,
            }
        )
        if desc is not UNSET:
            field_dict["desc"] = desc
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.engine_desc_meta import EngineDescMeta

        d = dict(src_dict)
        name = d.pop("name")

        type_ = ENGINETYPE(d.pop("type"))

        infer_type = INFERTYPE(d.pop("infer_type"))

        desc = d.pop("desc", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, EngineDescMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = EngineDescMeta.from_dict(_meta)

        engine_desc = cls(
            name=name,
            type_=type_,
            infer_type=infer_type,
            desc=desc,
            meta=meta,
        )

        engine_desc.additional_properties = d
        return engine_desc

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
