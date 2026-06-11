from pathlib import Path

root = Path('/mnt/data/site_v25_work')
career = root / 'career-os.html'
index = root / 'index.html'
changelog = root / 'CHANGELOG.md'

book5 = r'''

        <article class="card module-card" id="book-tool-005">
          <div class="module-head">
            <span class="module-no">BOOK TOOL 005 · OPERATIONAL RESILIENCE</span>
            <h3>أطر المرونة التشغيلية واحتواء الأزمات</h3>
            <span class="module-en">Everyday Resilience · Gail Gazelle, MD · 2020</span>
            <p class="module-why">الاستخلاص المهني من الكتاب: المرونة ليست تجنّب الإخفاقات، بل طريقة منظمة للمرور خلالها: فصل الحقائق عن الافتراضات، التوقف قبل رد الفعل، تهدئة التصعيد، وحماية طاقة الفريق حتى يستمر الأداء دون استنزاف.</p>
          </div>

          <div class="toolbox-grid">
            <article class="toolbox-card"><span class="decision-badge">01 · FACTS</span><h4>فصل الحدث عن الافتراض</h4><p>في أي تعثر، نميّز بين ما حدث فعلًا وبين القصة التي يبنيها الفريق حوله.</p><ul class="toolbox-list"><li>Incident Reframing Sheet</li><li>First Arrow / Second Arrow</li><li>دليل: 3 نماذج مراجعة موضوعية</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">02 · PAUSE</span><h4>التوقف التكتيكي قبل القرار</h4><p>دقيقة صمت منظمة قد تمنع قرارًا متسرعًا في اجتماع متوتر.</p><ul class="toolbox-list"><li>Purposeful Pause Meeting Card</li><li>هدف القرار + القيود الحالية</li><li>دليل: 5 توقفات موثقة</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">03 · STOP</span><h4>تهدئة التصعيد قبل الرد</h4><p>عند وصول تصعيد أو ملاحظة حادة، نكتب الرد ثم نراجعه بعد تهدئة قصيرة.</p><ul class="toolbox-list"><li>Escalation De-compression Checklist</li><li>Stop · Breathe · Observe · Proceed</li><li>دليل: سجل Draft vs Final</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">04 · INTENTION</span><h4>النوايا اليومية بجانب الأهداف</h4><p>الهدف يقول ماذا ننجز، والنية اليومية تقول كيف نحافظ على جودة السلوك أثناء التنفيذ.</p><ul class="toolbox-list"><li>Daily Leadership Intention Tracker</li><li>نية تشغيلية واحدة في بداية اليوم</li><li>دليل: 4 أسابيع من السجل</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">05 · FEEDBACK</span><h4>توازن التغذية الراجعة</h4><p>النقد وحده يضخم الانحياز السلبي؛ نبدأ بنقاط قوة موثقة ثم نحدد فجوة واحدة.</p><ul class="toolbox-list"><li>Strengths-Based Feedback Scorecard</li><li>3 نقاط قوة + فجوة تشغيلية</li><li>دليل: 3 جلسات Feedback موثقة</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">06 · REFRAME</span><h4>تفكيك النقد الذاتي المهني</h4><p>نحوّل جملة مثل “فشلت” إلى بيانات أداء: ماذا حدث؟ ما الذي يناقض الحكم؟ ما الخطوة؟</p><ul class="toolbox-list"><li>Cognitive Bias Reframing Log</li><li>افتراض نقدي + 3 بيانات موضوعية</li><li>دليل: جلستا Coaching منظمتان</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">07 · POST-MORTEM</span><h4>مراجعة ما بعد الحادث دون دفاعية</h4><p>نراجع الفشل كواقع تشغيلي لا كمحكمة لوم، ثم نحوله إلى سبب جذري وإجراء.</p><ul class="toolbox-list"><li>Non-Defensive Post-Mortem Template</li><li>Recognize · Allow · Investigate · Nurture</li><li>دليل: RCA واحد مكتمل</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">08 · CAPACITY</span><h4>حدود السعة والطاقة</h4><p>الاستدامة تحتاج حدودًا تشغيلية واضحة: ما العاجل فعلًا؟ ومتى لا نرسل؟</p><ul class="toolbox-list"><li>Team Capacity &amp; Boundary Checklist</li><li>بريد بعد الدوام + مهام نهاية الأسبوع</li><li>دليل: بروتوكول حدود تواصل</li></ul></article>
          </div>

          <div class="module-body" style="margin-top:28px">
            <details open>
              <summary>الأدوات الخمس الجاهزة <span class="sum-tag">READY TO USE</span></summary>
              <div class="mod-content">
                <div class="table-wrap">
                  <table class="decision-table">
                    <thead><tr><th scope="col">الأداة</th><th scope="col">استخدامها في 10 دقائق</th><th scope="col">الدليل الناتج</th></tr></thead>
                    <tbody>
                      <tr><td><strong>Incident Reframing Sheet</strong></td><td>اكتب الحقائق غير القابلة للجدل في عمود، ثم الافتراضات والمخاوف في عمود ثانٍ، ثم ابنِ خطوتين عمليتين من الحقائق فقط.</td><td>نموذج مراجعة يفصل الواقع التشغيلي عن اللوم والذعر.</td></tr>
                      <tr><td><strong>Purposeful Pause Meeting Card</strong></td><td>عند ارتفاع التوتر أو خروج الاجتماع عن المسار: توقف 60 ثانية واسأل: هل نناقش الجذر أم العرض؟ وما القرار المطلوب الآن؟</td><td>سجل توقف قبل القرار يوضح المشغل والقرار بعد التوقف.</td></tr>
                      <tr><td><strong>Strengths-Based Feedback Scorecard</strong></td><td>قبل أي ملاحظة تصحيحية، وثّق ثلاث نقاط قوة مبنية على بيانات، ثم اربط فجوة التحسين بها.</td><td>بطاقة Feedback آمنة ومحددة وغير دفاعية.</td></tr>
                      <tr><td><strong>Daily Leadership Intention Tracker</strong></td><td>في بداية اليوم: هدف قياسي واحد + نية سلوكية واحدة مثل وضوح التوثيق أو هدوء التواصل عند العائق.</td><td>سجل 5 أيام يربط السلوك اليومي بجودة التنفيذ.</td></tr>
                      <tr><td><strong>Team Capacity &amp; Boundary Checklist</strong></td><td>راجع اتصالات ما بعد الدوام والمهام الأسبوعية، ثم عرّف “طارئ” و“غير طارئ” بوضوح.</td><td>بروتوكول حدود تواصل يحمي الاستدامة دون تعطيل العمل.</td></tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </details>
            <details>
              <summary>خطة ممارسة 30 يومًا <span class="sum-tag">30-DAY PRACTICE</span></summary>
              <div class="mod-content">
                <ul class="compact-list">
                  <li><strong>الأسبوع 1 — التوقف قبل القرار:</strong> استخدم بطاقة التوقف الهادف في اجتماعين. المخرج: سجل يوضح المشغل والقرار بعد التوقف.</li>
                  <li><strong>الأسبوع 2 — فصل الحقائق عن الافتراضات:</strong> طبق نموذج إعادة التأطير على تعثر تشغيلي واحد. المخرج: ورقة تميّز الحقائق عن المخاوف.</li>
                  <li><strong>الأسبوع 3 — Feedback غير دفاعي:</strong> استخدم بطاقة نقاط القوة لصياغة مراجعة واحدة لفرد أو مورد أو عملية. المخرج: نموذج Feedback مجهول أو تعليمي.</li>
                  <li><strong>الأسبوع 4 — النية اليومية والتقرير:</strong> تتبع نية قيادية لمدة 5 أيام، ثم اكتب تقرير ممارسة من صفحة واحدة. المخرج: سجل نوايا + تقرير جاهزية.</li>
                </ul>
              </div>
            </details>
            <details>
              <summary>قالب تقرير صفحة واحدة <span class="sum-tag">ONE-PAGE REPORT</span></summary>
              <div class="mod-content">
                <ol class="report-template">
                  <li><strong>منطقة التركيز:</strong> إعادة التأطير المعرفي واحتواء التصعيد التشغيلي.</li>
                  <li><strong>الأدوات المستخدمة:</strong> Purposeful Pause، Incident Reframing، Strengths-Based Feedback، Daily Intention، Capacity Boundary.</li>
                  <li><strong>الأدلة المسجلة:</strong> عدد نماذج إعادة التأطير، عدد توقفات القرار، عدد بطاقات Feedback، وعدد أيام النية اليومية.</li>
                  <li><strong>ملاحظة تشغيلية:</strong> ما الذي تغير في جودة النقاش أو سرعة العودة إلى القرار؟</li>
                  <li><strong>حدود التقرير:</strong> هذا توثيق ممارسة إدارية، وليس نصيحة نفسية أو ضمانًا لنجاح المشاريع.</li>
                  <li><strong>الفعل التالي:</strong> أداة واحدة ستستمر الشهر القادم، وتعديل واحد سيطبق في الاجتماعات.</li>
                </ol>
              </div>
            </details>
            <details>
              <summary>جملة سيرة وLinkedIn آمنة <span class="sum-tag">SAFE WORDING</span></summary>
              <div class="mod-content">
                <div class="cv-snippet">Documented and practiced operational resilience frameworks, including structured decision-making pauses and objective incident reframing, to align team focus and manage execution during high-pressure workflows.</div>
                <p><strong>LinkedIn:</strong> خلال الفترة الماضية، ركزت على تطبيق وتوثيق أطر عمل مستمدة من مفاهيم المرونة التشغيلية: أدوات تفصل بين التحديات الواقعية والافتراضات، وتدعم اتخاذ القرار الهادئ في بيئة العمل.</p>
                <p><strong>بيان الأمان:</strong> هذه الأدوات ليست علاجًا نفسيًا ولا تقييمًا لأفراد الفريق. هي قوالب عمل لتقليل ردود الفعل المتسرعة، وتحسين مراجعة التعثرات، وحماية السعة التشغيلية بأدلة مكتوبة.</p>
              </div>
            </details>
          </div>
        </article>
'''

text = career.read_text(encoding='utf-8')
marker = '\n\n      </div>\n    </section>\n\n<section class="section" id="skill-modules">'
if marker not in text:
    raise SystemExit('Career insertion marker not found')
text = text.replace(marker, book5 + marker, 1)
career.write_text(text, encoding='utf-8')

idx = index.read_text(encoding='utf-8')
idx = idx.replace(
    'أضيف الآن مسار أدوات الكتب مع Book Tool 001 للثقة كأفعال صغيرة، وBook Tool 002 لتصفية الذهن وحماية التركيز، وBook Tool 003 لأنماط التفاعل كعدة تواصل وإسناد.',
    'أضيف الآن مسار أدوات الكتب مع Book Tools 001–005: الثقة كأفعال صغيرة، تصفية الذهن، أنماط التفاعل، التفاوض بالتعاطف، والمرونة التشغيلية.'
)
idx = idx.replace(
    '<p class="chosen">Confidence + Clear-Mind + Interaction + Negotiation</p>\n            <p>تحويل الكتب إلى أدوات عمل: بطاقة اجتماع، مواءمة توقعات، مصفوفة فرز، مراجعة أسبوعية، تخطيط تواصل، قرار إسناد، وأسئلة تفاوض تضمن التنفيذ.</p>',
    '<p class="chosen">Confidence + Clear-Mind + Interaction + Negotiation + Resilience</p>\n            <p>تحويل الكتب إلى أدوات عمل: بطاقة اجتماع، مواءمة توقعات، مراجعة أسبوعية، تخطيط تواصل، أسئلة تفاوض، وتوقف تكتيكي يفصل الحقائق عن الافتراضات وقت الضغط.</p>'
)
index.write_text(idx, encoding='utf-8')

prompt = '''You are continuing the existing static website ZIP:
AquaClimate Lab × إشارات الجسد
Career-OS Toolbox | Book-Derived Leadership Tools

Current source of truth:
aquaclimatelab_site_v25_book_tool_005_resilience.zip

Final polish only. Do not restart. Do not convert to a framework. Static HTML + CSS + JS only.

New addition:
Book Tool 005 — Operational Resilience & De-escalation Frameworks
أطر المرونة التشغيلية واحتواء الأزمات
Source extraction: Everyday Resilience — Gail Gazelle, MD, 2020.

Check and improve only:
1. Arabic RTL readability.
2. Mobile spacing for Book Tool 005 cards and tables.
3. Ensure Book Tools 001–005 read as one coherent series.
4. Ensure Book Tool 005 sounds like operational leadership tools, not clinical/psychological advice.
5. Ensure the resilience section keeps safety wording: no therapy, no diagnosis, no guarantees, no confidential data.
6. Verify internal anchors and homepage card.
7. Verify Water Wonder links and PDFs remain untouched.
8. Verify no blocked career-outcome wording is reintroduced.

Return:
- ready-to-deploy ZIP
- changed files list
- confirmation static HTML/CSS/JS only
- confirmation links/PDFs/emails preserved
'''
(root / 'CLAUDE_FABLE_V25_BOOK_TOOL_005_PROMPT.md').write_text(prompt, encoding='utf-8')

with changelog.open('a', encoding='utf-8') as f:
    f.write('\n\n## v25 — Book Tool 005: Operational Resilience\n')
    f.write('- Added Book Tool 005 under Book-Derived Leadership Tools.\n')
    f.write('- Converted Everyday Resilience extraction into operational leadership tools: incident reframing, purposeful pause, escalation decompression, daily intention tracking, feedback scorecard, and capacity boundaries.\n')
    f.write('- Updated homepage Book Tools teaser to include resilience.\n')
    f.write('- Added Claude final-polish prompt for v25.\n')

print('done')
