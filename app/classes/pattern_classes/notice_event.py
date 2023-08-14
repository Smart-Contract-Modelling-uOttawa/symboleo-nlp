from app.classes.pattern_classes.pattern_class import EventPatternClass, PatternVariable as PV

class NoticeEvent(EventPatternClass):
    sequence = [PV.CONDITIONAL_N, PV.TIMESPAN, PV.NOTICE_EVENT]