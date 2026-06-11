from pathlib import Path
import zipfile, os, re

root = Path('/mnt/data/site_v26_work')
career = root / 'career-os.html'
index = root / 'index.html'
changelog = root / 'CHANGELOG.md'

book6 = r'''

        <article class="card module-card" id="book-tool-006">
          <div class="module-head">
            <span class="module-no">BOOK TOOL 006 · EXECUTION &amp; PERFORMANCE ALIGNMENT OS</span>
            <h3>نظام التوافق اليومي وتقييم الأداء المهني</h3>
            <span class="module-en">High Performance Planner · Brendon Burchard</span>
            <p class="module-why">الاستخلاص المهني من الملف: الأداء العالي لا يُترك للذاكرة أو المزاج اليومي؛ بل يتحول إلى طقس قصير: تحديد 3 أولويات، توقع عائق واحد، دعم عضو واحد، مراجعة نهاية اليوم، ثم بطاقة أسبوعية تقيس الوضوح والإنتاجية والتأثير والشجاعة المهنية.</p>
          </div>

          <div class="toolbox-grid">
            <article class="toolbox-card"><span class="decision-badge">01 · DAILY 3</span><h4>النية اليومية وتحديد الأولويات</h4><p>ابدأ اليوم قبل البريد والتنبيهات بثلاث نتائج مهنية فقط، وفعل واحد يعبّر عن جودة الأداء.</p><ul class="toolbox-list"><li>Daily Alignment Checklist</li><li>Top 3 Professional Goals</li><li>دليل: سجل يومي مرتبط بمخرجات المشروع</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">02 · ANTICIPATE</span><h4>استباق المشكلات قبل ظهورها</h4><p>كل يوم له عائق محتمل: تأخير، توتر، طلب مفاجئ، أو قرار غير واضح. نكتبه قبل أن يتحول إلى ارتباك.</p><ul class="toolbox-list"><li>Risk Anticipation Card</li><li>عائق محتمل + استجابة مهنية</li><li>دليل: مقارنة المتوقع بالواقع</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">03 · TEAM</span><h4>التواصل المقصود مع الفريق</h4><p>القيادة اليومية ليست اجتماعًا كبيرًا دائمًا؛ أحيانًا هي دعم محدد لعضو واحد يحتاج توجيهًا أو تحديًا مناسبًا.</p><ul class="toolbox-list"><li>Team Connection Sheet</li><li>من يحتاج دعمي اليوم؟</li><li>دليل: ملاحظات 1-on-1 منظمة</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">04 · FOCUS</span><h4>إدارة الطاقة والتركيز</h4><p>نقيس أين يذهب وقت التركيز: عمل عميق أم ردود فعل؟ ثم نحمي كتلة تركيز واحدة بدل مطاردة كل شيء.</p><ul class="toolbox-list"><li>Focus &amp; Energy Audit</li><li>Deep Work vs Reactive Tasks</li><li>دليل: جدول فترات تركيز</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">05 · COURAGE</span><h4>الشجاعة المهنية والمبادرة</h4><p>في الغموض لا ننتظر وضوحًا كاملًا. نكتب القرار الصغير الذي يحرك العمل خطوة واحدة.</p><ul class="toolbox-list"><li>Decision &amp; Action Log</li><li>منطقة غموض + فعل محدد</li><li>دليل: قرارات موثقة تحت عدم اليقين</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">06 · RETRO</span><h4>مراجعة نهاية اليوم</h4><p>نهاية اليوم ليست لومًا للذات؛ هي التقاط درس واحد وتحسين واحد للغد.</p><ul class="toolbox-list"><li>End-of-Day Retrospective Log</li><li>ما نجح؟ ماذا تعلمت؟ ماذا أحسن؟</li><li>دليل: سجل دروس تشغيلية</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">07 · REFRAME</span><h4>إعادة صياغة تحدي الأسبوع</h4><p>عندما أكتب نصيحتي لشخص آخر يواجه نفس المشكلة، أرى الموقف بموضوعية أكبر.</p><ul class="toolbox-list"><li>Weekly Mentorship Reframe</li><li>تحدي الأسبوع + نصيحة موضوعية</li><li>دليل: ملف تحديات وحلول</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">08 · SCORE</span><h4>بطاقة تقييم العادات المهنية</h4><p>التحسن يحتاج خط أساس. نقيم الوضوح، الإنتاجية، التأثير، والشجاعة بدرجة بسيطة للمراجعة لا للمبالغة.</p><ul class="toolbox-list"><li>Professional Habit Scorecard</li><li>Clarity · Productivity · Influence · Courage</li><li>دليل: نقاط شهرية للمراجعة</li></ul></article>
          </div>

          <div class="module-body" style="margin-top:28px">
            <details open>
              <summary>الأدوات الخمس الجاهزة <span class="sum-tag">READY TO USE</span></summary>
              <div class="mod-content">
                <div class="table-wrap">
                  <table class="decision-table">
                    <thead><tr><th scope="col">الأداة</th><th scope="col">استخدامها في 10 دقائق</th><th scope="col">الدليل الناتج</th></tr></thead>
                    <tbody>
                      <tr><td><strong>Daily Alignment Checklist</strong></td><td>قبل البريد: اكتب 3 أهداف مهنية لليوم، عضوًا يحتاج دعمك، عائقًا محتملًا، وطريقة استجابة هادئة.</td><td>سجل توافق يومي يربط المهام بأهداف الفريق.</td></tr>
                      <tr><td><strong>End-of-Day Retrospective Log</strong></td><td>آخر اليوم: موقف أُدير جيدًا، درس تشغيلي، وتحسين واحد يجعل الغد أكثر فعالية.</td><td>سجل دروس تشغيلية لا يعتمد على الذاكرة.</td></tr>
                      <tr><td><strong>Weekly Mentorship Reframe</strong></td><td>اكتب تحدي الأسبوع، ثم اكتب النصيحة التي كنت ستعطيها لزميل يواجه نفس التحدي.</td><td>ورقة تحليل موضوعية للتحديات المتكررة.</td></tr>
                      <tr><td><strong>Professional Habits Scorecard</strong></td><td>قيّم من 1 إلى 5: الوضوح، الإنتاجية، التأثير، والشجاعة المهنية، ثم اختر فجوة واحدة للشهر التالي.</td><td>بطاقة قياس أسبوعية قابلة للمقارنة.</td></tr>
                      <tr><td><strong>Monthly Mission &amp; Learning Assessment</strong></td><td>قيّم وضوح قيمة الدور والتعلم المهني من 1 إلى 10، ثم اختر عادة واحدة لتحسين الدورة القادمة.</td><td>تقييم شهري يربط المهمة بالتعلم والتحسن.</td></tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </details>
            <details>
              <summary>خطة ممارسة 30 يومًا <span class="sum-tag">30-DAY PRACTICE</span></summary>
              <div class="mod-content">
                <ul class="compact-list">
                  <li><strong>الأسبوع 1 — التوافق اليومي:</strong> استخدم Daily Alignment Checklist كل صباح. المخرج: 5 سجلات يومية تحدد 3 أولويات وعائقًا محتملًا.</li>
                  <li><strong>الأسبوع 2 — مراجعة نهاية اليوم:</strong> خصص 10 دقائق في نهاية كل يوم لتوثيق درس وتحسين. المخرج: 5 سجلات Retrospective.</li>
                  <li><strong>الأسبوع 3 — إعادة صياغة التحديات:</strong> حلل أكبر عائق أسبوعي كأنك تنصح زميلًا. المخرج: وثيقة Weekly Mentorship Reframe واحدة.</li>
                  <li><strong>الأسبوع 4 — بطاقة العادات والتقييم الشهري:</strong> نفّذ Professional Habits Scorecard وMonthly Assessment. المخرج: بطاقة رقمية واحدة وخطة عادة للشهر التالي.</li>
                </ul>
              </div>
            </details>
            <details>
              <summary>قالب تقرير صفحة واحدة <span class="sum-tag">ONE-PAGE REPORT</span></summary>
              <div class="mod-content">
                <ol class="report-template">
                  <li><strong>الهدف:</strong> توثيق ممارسة التوافق اليومي، استباق المخاطر، والمراجعة الأسبوعية خلال 30 يومًا.</li>
                  <li><strong>الأدوات المستخدمة:</strong> Daily Alignment، End-of-Day Retrospective، Weekly Mentorship Reframe، Professional Habit Scorecard.</li>
                  <li><strong>الأدلة المنتجة:</strong> عدد سجلات الأولويات، عدد سجلات نهاية اليوم، بطاقة تقييم واحدة، وتقييم تعلم شهري.</li>
                  <li><strong>ملاحظة قابلة للملاحظة:</strong> هل أصبحت الأولويات أكثر وضوحًا؟ هل قلّت ردود الفعل العشوائية؟ هل ظهرت فجوة واحدة متكررة؟</li>
                  <li><strong>حدود التقرير:</strong> هذا توثيق ممارسة ذاتية منظمة، وليس قياسًا رسميًا للأداء ولا ضمانًا لنتائج العمل.</li>
                  <li><strong>الفعل التالي:</strong> عادة مهنية واحدة سيتم تحسينها في الدورة التالية.</li>
                </ol>
              </div>
            </details>
            <details>
              <summary>جملة سيرة وLinkedIn آمنة <span class="sum-tag">SAFE WORDING</span></summary>
              <div class="mod-content">
                <div class="cv-snippet">Practiced and documented professional alignment frameworks, producing daily prioritization checklists and weekly operational scorecards to track process execution.</div>
                <p><strong>LinkedIn:</strong> تم ممارسة وتوثيق نماذج عملية لتنظيم الأولويات اليومية، وتقييم الأداء الأسبوعي بأسلوب رقمي، وتوثيق الدروس التشغيلية المستفادة لتعزيز بيئة العمل المنظمة.</p>
                <p><strong>بيان الأمان:</strong> هذه الوحدة لا تدّعي إتقان الأداء العالي ولا تضمن نتائج المشاريع. هي قوالب يومية وأسبوعية لبناء وضوح، تركيز، ومراجعة قابلة للتوثيق.</p>
              </div>
            </details>
          </div>
        </article>
'''

text = career.read_text(encoding='utf-8')
marker = '\n\n\n      </div>\n    </section>\n\n<section class="section" id="skill-modules">'
if marker not in text:
    marker = '\n\n      </div>\n    </section>\n\n<section class="section" id="skill-modules">'
if marker not in text:
    raise SystemExit('Career insertion marker not found')
text = text.replace(marker, book6 + marker, 1)
career.write_text(text, encoding='utf-8')

idx = index.read_text(encoding='utf-8')
idx = idx.replace(
    'أضيف الآن مسار أدوات الكتب مع Book Tools 001–005: الثقة كأفعال صغيرة، تصفية الذهن، أنماط التفاعل، التفاوض بالتعاطف، والمرونة التشغيلية.',
    'أضيف الآن مسار أدوات الكتب مع Book Tools 001–006: الثقة كأفعال صغيرة، تصفية الذهن، أنماط التفاعل، التفاوض بالتعاطف، المرونة التشغيلية، ونظام التوافق اليومي وتقييم الأداء.'
)
idx = idx.replace(
    '<p class="chosen">Confidence + Clear-Mind + Interaction + Negotiation + Resilience</p>\n            <p>تحويل الكتب إلى أدوات عمل: بطاقة اجتماع، مواءمة توقعات، مراجعة أسبوعية، تخطيط تواصل، أسئلة تفاوض، وتوقف تكتيكي يفصل الحقائق عن الافتراضات وقت الضغط.</p>',
    '<p class="chosen">Confidence + Clear-Mind + Interaction + Negotiation + Resilience + Performance</p>\n            <p>تحويل الكتب إلى أدوات عمل: بطاقة اجتماع، مواءمة توقعات، مراجعة أسبوعية، تخطيط تواصل، أسئلة تفاوض، توقف تكتيكي، وسجل توافق يومي يربط الأولويات بالتنفيذ.</p>'
)
index.write_text(idx, encoding='utf-8')

prompt = '''You are continuing the existing static website ZIP:
AquaClimate Lab × إشارات الجسد
Career-OS Toolbox | Book-Derived Leadership Tools

Current source of truth:
aquaclimatelab_site_v26_book_tool_006_performance_alignment.zip

Final polish only. Do not restart. Do not convert to a framework. Static HTML + CSS + JS only.

New addition:
Book Tool 006 — Execution & Performance Alignment OS
نظام التوافق اليومي وتقييم الأداء المهني
Source extraction: High Performance Planner — Brendon Burchard.

Check and improve only:
1. Arabic RTL readability.
2. Mobile spacing for Book Tool 006 cards and tables.
3. Ensure Book Tools 001–006 read as one coherent series.
4. Ensure Book Tool 006 feels like a practical execution system, not motivational content.
5. Keep safety wording: no guaranteed results, no official performance evaluation claims, no confidential data.
6. Verify internal anchors and homepage card.
7. Verify Water Wonder links and PDFs remain untouched.
8. Verify blocked career-outcome wording remains absent from all files.

Return:
- ready-to-deploy ZIP
- changed files list
- confirmation static HTML/CSS/JS only
- confirmation links/PDFs/emails preserved
'''
(root / 'CLAUDE_FABLE_V26_BOOK_TOOL_006_PROMPT.md').write_text(prompt, encoding='utf-8')

with changelog.open('a', encoding='utf-8') as f:
    f.write('\n\n## v26 — Book Tool 006: Performance Alignment OS\n')
    f.write('- Added Book Tool 006 under Book-Derived Leadership Tools.\n')
    f.write('- Converted High Performance Planner extraction into daily alignment and professional habit tools: priorities, risk anticipation, team connection, energy/focus, daily retrospective, weekly reframe, and scorecards.\n')
    f.write('- Updated homepage Book Tools teaser to include performance alignment.\n')
    f.write('- Added Claude final-polish prompt for v26.\n')

print('applied book tool 006')
