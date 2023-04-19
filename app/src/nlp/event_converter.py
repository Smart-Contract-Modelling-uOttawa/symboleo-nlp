from app.classes.spec.declaration import Declaration, DeclarationProp
from app.src.nlp.verb_extractor import IExtractVerb


# Will remove this. But keep it for now to transfer code over 

class IConvertDeclarationToEvent:
    def convert(self, declaration: Declaration):
        raise NotImplementedError()

class DeclarationToEventConverter(IConvertDeclarationToEvent):
    def __init__(self, verb_extractor: IExtractVerb):
        self.__verb_extractor = verb_extractor
    
    def convert(self, declaration: Declaration):
        props = declaration.props
        prop_dict = {x.key: x for x in props}

        # Find the subject

        subject_prop_names = ['agent', 'from']
        for spn in subject_prop_names:
            if spn in prop_dict:
                subject = prop_dict[spn].value
                del prop_dict[spn]
        
        # Find the dobj
        ## Paid ==> currency + amount
        ## What type of verb is paid
        ## I think we need framenet... Lets see if that stores any important linguistic information...
        
        




        ## depends on the verb... if pay.. then its 'to'
        ## This is where we may need to use framenet
        ## In some cases, it is also a combo - e.g. currency/amount
        ## would be super easy to just create a mapping. 
        ### If event is Paid... then just map everything in a predictable way

        dobj_prop_names = ['target', 'to', 'recipient']
        for dpn in dobj_prop_names:
            if dpn in prop_dict:
                dobj = prop_dict[dpn].value
                del prop_dict[dpn]
        
        # Get the verb
        evt_name = declaration.base_type.lower()
        verb = self.__verb_extractor.extract(evt_name)
        
        evt_props = []
        for x in prop_dict:
            p = prop_dict[x]
            next_prop = (p.key, p.value, p.type)
            evt_props.append(next_prop)


        return (subject, verb, dobj, evt_props)
    
