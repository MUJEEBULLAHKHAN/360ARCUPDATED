from django import forms
from django.forms import widgets
from .models import *

CHOICES=[('Yes/نعم','Yes/نعم'),
         ('No/لا','No/لا')]
class arcinfoForm(forms.ModelForm):
    company = forms.CharField(label='Company Name :/اسم الشركة')
    owner = forms.CharField(label='Owner Name/اسم المالك')
    contact = forms.CharField(label='Owner Contact :/رقم التواصل بالمالك')
    manager = forms.CharField(label='Manager Name :/اسم المدير')
    managercont = forms.CharField(label='Manager contacts /رقم التواصل بالمدير')
    estimate = forms.ChoiceField(choices=CHOICES,label='Computerized Estimating program :/هل يوجد برنامج تقدير محوسب', widget=forms.RadioSelect())
    class Meta:
        model = arcinfo
        fields = '__all__'

class arclocForm(forms.ModelForm):
    address = forms.CharField(label='address عنوان')
    class Meta:
        model = arcloc
        fields = '__all__'

class financialForm(forms.ModelForm):
    labor = forms.CharField(label='Labor Sales / Month /مبيعات اجور اليد / شهريا')
    part = forms.CharField(label='Parts Sales / Month /مبيعات قطع الغيار / شهريا')
    material = forms.CharField(label='Material Sales / Month /مبيعات المواد / شهريا')
    rent = forms.CharField(label='Rent /Month / الإيجار / شهريا')
    productive = forms.CharField(label='Staff Cost /Month Productive :/تكلفة العمالة / شهريا')
    support = forms.CharField(label='Staff Cost /Month Support:/ تكلفة الاداريين / شهريا')
    month = forms.CharField(label='Other Expenses / Month:/مصاريف أخرى / شهريا')
    class Meta:
        model = financial
        fields = '__all__'


class workforceinfoForm(forms.ModelForm):
    PPE = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Staff provided with PPE: /معدات الوقاية الشخصية ')
    denter = forms.CharField(label='Number of Denters :/عدد السمكرية :')
    painter = forms.CharField(label='Number of Painters :/عدد الدهانيين :')
    elec = forms.CharField(label='Number of Mechanic/Elec :/عدد الميكانيكية - الكهربائية ')
    staff = forms.CharField(label='Number of Support staff:/عدد موظفي الادارة')
    workbays = forms.CharField(label='Number of workbays :/عدد اماكن العمل داخل الورشة - الطاقة الاستيعابية للورشة:')
    body = forms.CharField(label='Number of Jobs / Month Bodyshop only :/انتاجية الورشة في ما يخص السمكرة و الدهان - شهريا')
    nonbody = forms.CharField(label='Number of Jobs / Month Non bodyshop only :/ انتاجية الورشة اعمال غير السمكرة و الدهان - شهريا:')
    sqm = forms.CharField(label='Workshop Size Sqm :/ مساحة الورشة - متر مربع:')
    insurance = forms.CharField(label='WP - Insurance % :/% نسبة العمل مع شركات التأمين')
    walkin = forms.CharField(label='WP - Walk-in % :/ % نسبة العمل مع العملاء الكاش - النقدي')
    fleet = forms.CharField(label='WP - Fleet % :/% شركات التي تمتلك اساطيل- شركات تاجير و وغيرها')
    park = forms.CharField(label='Number of Customer Parking :/ عدد مواقف السيارات للعملاء')
    recep = forms.CharField(label='Adequate Reception :/مكتب استقبال مناسب')
    wash = forms.CharField(label='Adequate Washroom - Customers:/ حمام مناسب - للعملاء')
    washstaff = forms.CharField(label='Adequate Washroom - Staff :/حمام مناسب - طاقم عمل')
    scrap = forms.CharField(label='Scrap storage :/منطقة تخزين الاسكراب')
    newpart = forms.CharField(label='New parts Storage :/منطقة تخزين قطع غيار جديدة')
    oilstorage = forms.CharField(label='Used Oil Storage :/منطقة تخزين الزيوت المستعملة')
    class Meta:
        model = workforceinfo
        fields = '__all__'


class repairinfoForm(forms.ModelForm):
    measure = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Estimates with 3D Measurement :/ نظام قياس ثلاثي الابعاد :')
    nonstruct = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Body repair - Non Structural Repairs :/ إصلاح الجسم - الإصلاحات غير الهيكلية ')
    struct = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Body repair - Structural Repairs :/ إصلاح الجسم - الإصلاحات الهيكلية :')
    paint = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Refinishing - Paint - Full :/ خدمات الدهان كاملة:')
    ac = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='General Electric Service / AC :/: خدمات الكهرباء و التكيف')
    body = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Aluminum Body Repair :/ إصلاح الألومنيوم :')
    qc = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='QC Report with 3D measurement :/: تقرير مراقبة الجودة مع قياسات ثلاثية الابعاد')
    brakes = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='General Repairs - Brakes/Suspension :/ الإصلاحات العامة - الفرامل / نظام التعليق :')
    tyre = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Tire Service :/خدمة الإطارات ')
    wheel = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Wheel Alignment :/وزن الاذرعة :')
    computer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Computer Diagnostic / Calibration/Repairs:/التشخيص / المعايرة الحاسوبية :')
    adas = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='ADAS (Advance Driver Assistance System) :/ اصلاح نظام الامان و مساعدة السائق :')
    engine = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Engine / Drive train Overhaul :/إصلاح المحرك / لرفع المحرك و نقله :')
    plastic = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Plastic Parts Repair :/إصلاح الأجزاء البلاستيكية :')
    welder = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label='Plastic Repair Tools- Hot Stapler, Hot Air Welder, Plastic Brazing:/أدوات إصلاح البلاستيك - دباسة ساخنة ، آلة لحام بالهواء الساخن ، لحام بلاستيك :')
    class Meta:
        model = repairinfo
        fields = '__all__'

class equipinfoForm(forms.ModelForm):
    it = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="IT system for Managing Workshop :/نظام حاسوبي لإدارة الورشة ")
    comp = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Computerized Estimation system :/نظام تقدير حاسوبي")
    access = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Access to vehicle measurement DATA sheet :/هل يوجد صلاحية للدخول لمعلومات قياسات السيارات من الشركات العالمية (شاصيه)")
    oem = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Access to OEM Repair Manuals (OEM) :/ الوصول إلى كتيبات إصلاح OEM")
    guide = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Access to OEM Labor time Guide (OEM) :/الوصول إلى دليل وقت عمل OEM")
    lift = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Two Post Lifts :/ رافعة بعامودين")
    frame = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Frame / Unibody structure alignment system :/ نظام اصلاح الشاصي")
    four = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="FOUR point anchoring system - Unibody :/ نظام إرساء ذو أربع نقاط- قطعة واحدة")
    anchor = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="FOUR point anchoring system - Frame :/نظام إرساء ذو أربع نقاط / إطار")
    ton = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="10 ton Pulling system :/ نظام سحب 10 طن")
    oxy = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Oxy/Acetylene Welding Equipment :/معدات لحام الأكسجين / الأسيتيلين")
    resistance = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Resistance / Spot Welding Equipment :/معدات لحام بتقنيةمقاومة المغنطه")
    heater = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Induction Heater :/ سخان الحث")
    plasma = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Plasma cutter :/ قاطعه بتقنية البلازما")
    mig = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="MIG welder Steel :/ لحام مخصص للفولاذ")
    dent = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Dent Puller - Steel :/ دنت بولير - فولاذ")
    air = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Air compressor :/ ضاغط الهواء")
    chain = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Chain Block / Port-A-Power:/سلسلة السحب")
    charging = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="AC Charging / Recovery Equipment :/ معدات شحن الفريون/ استعادة التيار المتردد")
    kit = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Denter Tools KIT :/ مجموعة أدوات السمكرة")
    dry = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Dry Sanding Equipment :/ معدات الصنفرة الجافة")
    hvlp = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="HVLP Spray Guns :/مسدسات الرش HVLP")
    vet = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Wet/Dry Vacuum Machines :/ ماكينات تنظيف جاف / رطب")
    booth = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Paint Booth :/ فرن لرش السيارات")
    prep = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Prep Station :/محطة تجهييز المركبة")
    mixing = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Paint Mixing Room fully equipped :/ غرفة خلط الدهان مجهزة بالكامل")
    tools = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Painter Tools Kit :/ طقم أدوات الرش")
    toolkit = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Electrician Tool Kit :/ طقم أدوات كهربائية")
    lifts = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Four Post Lifts - for Wheel Alignment :/ رافعات عامودية - لوزن الاذرعة")
    align = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Wheel Aligning Equipment :/ جهاز وزن الاذرعه")
    rise = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Low Rise Lift :/ رافعة منخفضة الارتفاع")
    changer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Tire Changer :/ مغير الاطارات")
    balancer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Wheel Balancer :/ ترصيص الكفرات")
    lathe = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Brake Lathe :/ مخرطة الفرامل")
    notes = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),label="Notes : Recommendation for Betterment in tools/service etc. /.ملاحظات : توصية لتحسين الأدوات/ الخدمات وما إلى ذلك")
    ch = forms.MultipleChoiceField(choices=[('reading', 'Reading'),('sports', 'Sports'),('music', 'Music'),('travel', 'Travel'),], widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = equipinfo
        fields = '__all__'

ch1=[('N/A - لايوجد', 'N/A - لايوجد'),('4star/اربع نجوم', '4star/اربع نجوم'),]
ch2=[('star/نجمة', 'star/نجمة'),('2star/نجمتين', '2star/نجمتين'),('3star/ثلاث نجوم', '3star/ثلاث نجوم'),('4star/اربع نجوم', '4star/اربع نجوم'),]
ch3=[('N/A - لايوجد', 'N/A - لايوجد'),('3star/ثلاث نجوم', '3star/ثلاث نجوم'),('4star/اربع نجوم', '4star/اربع نجوم'),]

class recepForm(forms.ModelForm):
    r1 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='computerized system to manage data, customers, vehicles, repair, operations and spare parts/ نظام حاسوبي لإدارة المنشأة يحتوي على بيانات : العملاء والمركبات وعملية الإصلاح والقطع المستبدلة')
    r2 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a quality control system./توفير نظام لإدارة الجودة')
    r3 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a reception area separate from the workshop provided with new suitable furniture./وجود منطقة استقبال مفصولة عن الورشة مزوَّدة بأثاث جيد ومتناسق ، مع خلو الجدران والاسقف والأرضيات من العيوب .')
    r5 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide waiting areas for women only/وجود منطقة مخصصة لانتظار النساء')
    r7 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a hot/cool conditioning system./وجود نظام تكييف حار/بارد.')
    r8 = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='Place all operation licenses and classification certificates clearly and according to instructions/ تثبيت جميع رخص التشغيل وشهادة التصنيف بشكل واضح وحسب التعليمات .')
    r10 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Place the guarantee policy clearly/ تثبيت سياسة الضمان بشكل واضح.')
    r12 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Place the communication number for complaints/ تثبيت رقم للتواصل عند وجود شكوى.')
    r14 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide special offices for receiving and delivering vehicles/ وجود مكاتب خاصة باستلام المركبات وأخرى خاصة بالتسليم.')
    r16 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Reception area should be in a good condition/ أن تكون مكاتب الاستقبال بحالة جيدة ومتناسقة.')
    r18 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a suitable number of seats in a good condition for waiting customers/وجود مقاعد متناسقة لانتظار العملاء بعدد كافٍ وبحالة جيدة.')
    r20 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide means of hospitality for customers/توفير ضيافة للعملاء.')
    r21 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide suitable means of entertainment/توفير وسائل مناسبة للتسلية.')
    class Meta:
        model = recepinfo
        fields = '__all__'
        
class empForm(forms.ModelForm):
    EPPE = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='All employees wearing PPE/ ارتداء العاملين أدوات السلامة الشخصية.')
    all = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='All employees wearing a uniform/ارتداء العاملين زي رسمي موحد.')
    use = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Use of personal identification cards/ تعليق البطاقات التعريفية.')
    speak = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide at least one person who speaks Arabic and English/توفير شخص على الأقل يجيد اللغة العربية والإنجليزية')
    aid = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='Provide persons trained on first aid and implementing firefighting plan/ توفير أشخاص مدربين على الإسعافات الأولية وتنفيذ خطة مكافحة الحريق .')
    one = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='One engineer at least holding specialized engineering qualifications/وجود مهندس واحد – على الأقل - مختص حاصل على مؤهل هندسي.')
    highly = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide highly qualified maintenance technicians/وجود فنيي صيانة حاصلون على مؤهل علمي.')
    proof = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide an annual plan for training and developing employees and provide a proof with that effect/توفير خطة سنوية لتدريب العاملين وتطويرهم وتقديم ما يثبت ذلك')
    job = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Document employees’ names, along with job descriptions stating the job tasks and required competencies/توثيق أسماء العاملين مع وصف وظيفي يُبين المهام الوظيفية والكفاءة اللازمة .')
    repair = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a record for employees to identify repair operations/وجود سجل للعاملين يوضح عمليات الإصلاح التي قاموا بها')
    class Meta:
        model = empinfo
        fields = '__all__'

class servicesForm(forms.ModelForm):
    website = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a website describing the establishment’s location, working hours and contact numbers/توفير موقع إليكتروني يوضح موقع المنشأة وساعات العمل وأرقام التواصل .')
    telephone = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a telephone system for easy communication with various departments/توفيير نظام هاتفي (سنترال) يُسهل الاتصال بمختلف أقسام المنشأة .')
    appointment = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide appointment reservation service/توفير خدمة حجز المواعيد.')
    record = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a record of complaints and taken actions/وجود سجل للشكاوى والإجراءات المتخذة بشأنها.')
    system = forms.MultipleChoiceField(choices=ch3, widget=forms.CheckboxSelectMultiple,label='Provide a system for measuring customers satisfaction/توفير نظام لقياس مدى رضا العملاء عن الخدمة المقدَّمة')
    shall = forms.MultipleChoiceField(choices=ch3, widget=forms.CheckboxSelectMultiple,label='Inspect vehicle record condition before being entered in the establishment Shall be documented with the customer/ فحص المركبة تسجيل حالتها باستخدام قائمة تدقيق قبل دخولها للمنشأة، وتوثيق ذلك مع العميل')
    access = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Present to customer written report for performed repairs to clarify the replaced parts, financial costs, guarantee period /إعطاء العملاء تقرير عن عملية الإصلاح يوضح القطع المستبدلة وفترة الضمان وشروطة')
    cost = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Wash the vehicle after finishing the repair/غسيل المركبة بعد عملية الإصلاح.')
    wash = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide e-payment system approved by Saudi Central Bank (SAMA)/توفير وسائل الدفع الإلكتروني المعتمدة من البنك المركزي السعودي ساما -SAMA')
    sama = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide credit cards payment system/توفير نظام دفع النقود باستخدام البطاقات الائتمانية.')
    credit = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a clear and environment friendly strategy for discharging of wastes and spare parts/ توفير سياسة واضحة للتخلص من النفايات وقطع الغيار المستبدلة بطريقة لا تضر بالبيئة ')
    class Meta:
        model = servicesinfo
        fields = '__all__'

class facilitiesForm(forms.ModelForm):
    parka1 = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide parking areas for vehicles before or after repair process that shall be shaded and fenced/ مواقف ضمن حدود المنشأة لصف المركبات قبل أو بعد عملية الاصلاح ، على أن تكون مضللة ومسورة ')
    female = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Two clean and in good condition toilets for customers; one for male and the other for females/ دورتي مياه نظيفة وبحالة جيدة، على أن تكون مخصَّصة للعملاء، إحداهما مخصصة للرجال والأخرى للنساء ')
    mosq = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide a special area for praying in case there is no near mosque/توفير مساحة خاصة للصلاة عند عدم وجود مسجد قريب.')
    risk = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='Provide all equipment in a sound condition, clear of any defects that might represent a risk to its users/جميع الأجهزة بحالة سليمة وخالية من العيوب التي قد تشكل خطرا على مستخدميها.')
    class Meta:
        model = facilitiesinfo
        fields = '__all__'

class deviceForm(forms.ModelForm):
    calibrate = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Calibrate all equipment regularly by a third party/معايرة الأجهزة دورياً عن طريق طرف ثالث .')
    inspect = forms.MultipleChoiceField(choices=ch2, widget=forms.CheckboxSelectMultiple,label='Inspect the equipment regularly by the establishment/فحص الأجهزة دورياً من قبل المنشأة ')
    provide = forms.MultipleChoiceField(choices=ch1, widget=forms.CheckboxSelectMultiple,label='Provide the minimum devices and equipment required to perform repair procedures /توفير الحد الأدنى من الأجهزة والمعدات للقيام بعملية الإصلاح')
    class Meta:
        model = deviceinfo
        fields = '__all__'