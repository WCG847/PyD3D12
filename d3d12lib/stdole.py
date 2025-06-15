from enum import IntFlag

from . import OLE as __wrapper_module__
from .OLE import (
    EXCEPINFO, OLE_XPOS_PIXELS, OLE_YPOS_HIMETRIC, BSTR, Color,
    OLE_XPOS_HIMETRIC, OLE_OPTEXCLUSIVE, Monochrome, GUID,
    OLE_YPOS_PIXELS, VARIANT_BOOL, OLE_XSIZE_PIXELS,
    OLE_XSIZE_HIMETRIC, IFontEventsDisp, IEnumVARIANT, VgaColor,
    FONTNAME, FontEvents, OLE_ENABLEDEFAULTBOOL, dispid, IFont,
    DISPPARAMS, FONTITALIC, Default, OLE_YPOS_CONTAINER, CoClass,
    Unchecked, Font, Checked, IUnknown, OLE_COLOR, StdPicture,
    OLE_YSIZE_CONTAINER, typelib_path, IDispatch, DISPMETHOD,
    OLE_YSIZE_HIMETRIC, OLE_XPOS_CONTAINER, HRESULT, StdFont, Picture,
    FONTBOLD, Gray, OLE_YSIZE_PIXELS, IPicture, _check_version,
    FONTSIZE, IFontDisp, Library, IPictureDisp, OLE_CANCELBOOL,
    FONTUNDERSCORE, OLE_XSIZE_CONTAINER, OLE_HANDLE, COMMETHOD,
    DISPPROPERTY, FONTSTRIKETHROUGH, _lcid
)


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


__all__ = [
    'OLE_XPOS_PIXELS', 'OLE_YPOS_HIMETRIC', 'OLE_COLOR', 'Color',
    'OLE_XPOS_HIMETRIC', 'OLE_OPTEXCLUSIVE', 'StdPicture',
    'Monochrome', 'OLE_YSIZE_CONTAINER', 'typelib_path',
    'OLE_YPOS_PIXELS', 'OLE_XSIZE_PIXELS', 'OLE_YSIZE_HIMETRIC',
    'OLE_XSIZE_HIMETRIC', 'IFontEventsDisp', 'OLE_XPOS_CONTAINER',
    'Font', 'StdFont', 'Picture', 'FONTBOLD', 'Gray',
    'OLE_YSIZE_PIXELS', 'VgaColor', 'IPicture', 'FONTSIZE',
    'IFontDisp', 'Library', 'FONTNAME', 'OLE_CANCELBOOL',
    'LoadPictureConstants', 'FontEvents', 'OLE_ENABLEDEFAULTBOOL',
    'FONTUNDERSCORE', 'IPictureDisp', 'IFont', 'OLE_TRISTATE',
    'FONTITALIC', 'OLE_XSIZE_CONTAINER', 'Default', 'OLE_HANDLE',
    'OLE_YPOS_CONTAINER', 'Unchecked', 'FONTSTRIKETHROUGH', 'Checked'
]

