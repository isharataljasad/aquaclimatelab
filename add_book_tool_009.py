from pathlib import Path

root = Path('/mnt/data/site_v29_work')
career = root / 'career-os.html'
index = root / 'index.html'
changelog = root / 'CHANGELOG.md'

article = r'''

        <article class="card module-card" id="book-tool-009">
          <div class="module-head">
            <span class="module-no">BOOK TOOL 009 · INTENTIONAL LEADERSHIP ROUTINE</span>
            <h3>القيادة المقصودة: من المهمة الربعية إلى روتين العمل الموثق</h3>
            <span class="module-en">Live Intentionally · Harsh Strongman · 2019</span>
            <p class="module-why">هذه الوحدة لا تستخدم الكتاب كبرنامج تحسين شخصي، بل كحقيبة قيادة عملية: تعريف مهمة ربع سنوية، إزالة المهام منخفضة القيمة، بناء أول 30 دقيقة من يوم القائدة، رصد أنماط أداء الفريق، إعادة صياغة المشكلة قبل القرار، وبروتوكول تغذية راجعة مباشرة.</p>
          </div>

          <div class="toolbox-grid">
            <article class="toolbox-card"><span class="decision-badge">01 · MISSION</span><h4>تحديد المهمة القيادية</h4><p>الأداء يتحسن عندما يعرف الفريق لماذا يعمل هذا الربع وما المؤشر الذي يثبت التقدم.</p><ul class="toolbox-list"><li>Quarterly Mission Card</li><li>هدف + مؤشر + قرار يومي</li><li>دليل: بطاقة مهمة تُراجع أسبوعيًا</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">02 · REMOVE</span><h4>إزالة المشتتات من العمل</h4><p>بعض المهام تبدو إنتاجية لكنها لا تخدم الهدف: اجتماع بلا قرار، تقرير لا يُستخدم، أو ردود فورية تكسر التركيز.</p><ul class="toolbox-list"><li>Junk Task Audit</li><li>حذف / إعادة توجيه / تفويض</li><li>دليل: قائمة مهام أُعيد تنظيمها</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">03 · STARTUP</span><h4>الثلاثون دقيقة الأولى</h4><p>نبدأ اليوم بمراجعة الأولويات والعائق الأكبر والقرار المطلوب قبل الغرق في البريد والرسائل.</p><ul class="toolbox-list"><li>Leader’s First 30 Minutes</li><li>أولوية + عائق + قرار</li><li>دليل: سجل أسبوعين</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">04 · PATTERNS</span><h4>رصد أنماط أداء الفريق</h4><p>لا نعدل الجدول بالانطباع. نرصد متى يرتفع الأداء ومتى ينخفض وما الحدث السابق لكل نمط.</p><ul class="toolbox-list"><li>Weekly Pattern Log</li><li>أعلى طاقة / أدنى أداء</li><li>دليل: 3 أنماط متكررة</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">05 · REFRAME</span><h4>إعادة صياغة المشكلة قبل القرار</h4><p>نفصل ردة الفعل الأولى عن التفسير الأقرب للواقع، ثم نحدد المعلومة الناقصة والخطوة التالية.</p><ul class="toolbox-list"><li>Reframe Sheet</li><li>أسوأ تفسير / أرجح تفسير</li><li>دليل: ورقة لكل قرار مهم</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">06 · FEEDBACK</span><h4>ثقافة الملاحظة المباشرة</h4><p>القاعدة: الملاحظة تُقال لصاحبها مباشرة، تبدأ بالموقف لا بالشخص، وتُرفق باقتراح واحد.</p><ul class="toolbox-list"><li>Direct Feedback Protocol</li><li>محضر اتفاق الفريق</li><li>دليل: بطاقة قواعد مراجعة شهرية</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">07 · BLUEPRINT</span><h4>التخطيط اليومي كأداة قيادة</h4><p>هيكل اليوم يقلل تعب القرار ويجعل الفريق يعرف الوقت، النشاط، والمخرج المتوقع بدل السؤال المستمر.</p><ul class="toolbox-list"><li>Team Day Blueprint</li><li>وقت / نشاط / مخرج</li><li>دليل: 4 مخططات أسبوعية</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">08 · REVIEW</span><h4>مراجعة نهاية اليوم</h4><p>ما لا نراجعه لا نتعلم منه: إنجاز اليوم، ما يمكن تحسينه، قرار غير مريح، وأولى مهام الغد.</p><ul class="toolbox-list"><li>End-of-Day Review Log</li><li>4 أسئلة يومية</li><li>دليل: سجل 30 يومًا</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">09 · READING</span><h4>القراءة المهنية كاستخلاص أدوات</h4><p>لا نقرأ للتجميع؛ نقرأ لنستخرج أداة واحدة قابلة للتطبيق ومخرجًا يمكن قياسه.</p><ul class="toolbox-list"><li>Book-to-Tool Extraction Card</li><li>فكرة → أداة → أثر</li><li>دليل: 3 بطاقات من 3 مصادر</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">10 · VALUES</span><h4>وضوح القيم القيادية</h4><p>نقارن القيم المعلنة بقرارات حديثة: هل القرار يثبت القيمة أم يناقضها؟</p><ul class="toolbox-list"><li>Leadership Values Clarity Sheet</li><li>5 قيم + قرارات داعمة/مخالفة</li><li>دليل: مراجعة ربع سنوية</li></ul></article>
          </div>

          <div class="module-body" style="margin-top:28px">
            <details open>
              <summary>الأدوات الست الجاهزة <span class="sum-tag">READY TO USE</span></summary>
              <div class="mod-content">
                <div class="table-wrap">
                  <table class="decision-table">
                    <thead><tr><th scope="col">الأداة</th><th scope="col">استخدامها في 10 دقائق</th><th scope="col">الدليل الناتج</th></tr></thead>
                    <tbody>
                      <tr><td><strong>Quarterly Mission Card</strong></td><td>اكتب المهمة في جملة، مؤشر النجاح، والقرار اليومي الذي يخدمها.</td><td>بطاقة مهمة تُثبت في بداية الاجتماع الأسبوعي.</td></tr>
                      <tr><td><strong>Junk Task Audit</strong></td><td>احصر مهام منخفضة القيمة، ثم قرر: حذف، إعادة توجيه، تفويض، أو إبقاء.</td><td>قائمة مهام مع الوقت المسترد أو الإجراء المتخذ.</td></tr>
                      <tr><td><strong>Reframe Sheet</strong></td><td>قبل قرار مؤثر: ردة الفعل الأولى، أسوأ تفسير، أرجح تفسير، المعلومة الناقصة، والخطوة التالية.</td><td>ورقة قرار تقلل الاندفاع وتوثق سبب الانتظار أو التحرك.</td></tr>
                      <tr><td><strong>End-of-Day Review Log</strong></td><td>أجب عن إنجاز اليوم، ما كان يمكن تحسينه، قرار غير مريح، وأولى مهام الغد.</td><td>سجل يومي يكشف أنماط القرارات والفجوات.</td></tr>
                      <tr><td><strong>Weekly Pattern Log</strong></td><td>كل خميس: متى ارتفع الأداء؟ متى انخفض؟ ما الحدث السابق؟ وما الإجراء المقترح؟</td><td>جدول أنماط أسبوعي يوجه إعادة جدولة نشاط واحد على الأقل.</td></tr>
                      <tr><td><strong>Direct Feedback Protocol</strong></td><td>اتفاق فريق: الملاحظة تُقال لصاحبها، تبدأ بالموقف، وتنتهي باقتراح عملي.</td><td>محضر اتفاق وقائمة متابعة شهرية.</td></tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </details>
            <details>
              <summary>خطة ممارسة 30 يومًا <span class="sum-tag">30-DAY PRACTICE</span></summary>
              <div class="mod-content">
                <ul class="compact-list">
                  <li><strong>الأسبوع 1 — التأسيس:</strong> املأ بطاقة المهمة الربعية، طبّق بروتوكول أول 30 دقيقة يوميًا، وابدأ سجل المراجعة اليومية. المخرج: بطاقة مهمة + 5 سجلات يومية.</li>
                  <li><strong>الأسبوع 2 — الرصد:</strong> املأ سجل الأنماط، ونفّذ مراجعة المهام الفارغة مع الفريق. المخرج: سجل أنماط + قائمة مهام منخفضة القيمة مع إجراءات.</li>
                  <li><strong>الأسبوع 3 — التطبيق:</strong> طبّق ورقة إعادة الصياغة على قرار حقيقي، وناقش بروتوكول التغذية الراجعة. المخرج: ورقة قرار + بطاقة بروتوكول موثقة.</li>
                  <li><strong>الأسبوع 4 — المراجعة والتوثيق:</strong> راجع 4 أسابيع من الأنماط، اكتب تقرير ممارسة، واستخرج أداة من كتاب مهني. المخرج: تقرير صفحة واحدة + بطاقة Book-to-Tool.</li>
                </ul>
              </div>
            </details>
            <details>
              <summary>قالب تقرير صفحة واحدة <span class="sum-tag">ONE-PAGE REPORT</span></summary>
              <div class="mod-content">
                <ol class="report-template">
                  <li><strong>اسم الأداة والمصدر:</strong> الأداة القيادية المستخلصة من قراءة مهنية.</li>
                  <li><strong>مدة الممارسة:</strong> الفترة وتاريخ التقرير.</li>
                  <li><strong>الأثر المنتج:</strong> الأدوات أو الوثائق التي أُنتجت فعليًا.</li>
                  <li><strong>دليل الجاهزية:</strong> ما الذي تغير في السلوك القيادي الموثق؟</li>
                  <li><strong>الأنماط المرصودة:</strong> ثلاثة أنماط فقط، دون أسماء أو بيانات سرية.</li>
                  <li><strong>القرارات التي تأثرت بالأداة:</strong> قرار واحد أو قراران مع التاريخ.</li>
                  <li><strong>ما سيُطبق في الشهر التالي:</strong> ممارسة واحدة تستمر وأخرى تُعدّل.</li>
                </ol>
              </div>
            </details>
            <details>
              <summary>جملة سيرة وLinkedIn آمنة <span class="sum-tag">SAFE WORDING</span></summary>
              <div class="mod-content">
                <div class="cv-snippet">Built and practiced a set of structured leadership tools derived from professional reading, including daily review logs, team task audits, decision reframing sheets, and quarterly mission cards, producing documented artifacts over a 30-day practice cycle.</div>
                <p><strong>LinkedIn:</strong> طورت مجموعة من الأدوات القيادية العملية المستخلصة من القراءة المهنية المنظمة، وطبقتها خلال دورة ممارسة موثقة بمدة ثلاثين يومًا، شملت سجلات المراجعة اليومية، ومراجعة أولويات الفريق، وبروتوكولات التغذية الراجعة.</p>
                <p><strong>بيان الأمان:</strong> هذه الوحدة لا تنقل نصوصًا من الكتاب، ولا تستخدم سياقًا شخصيًا، ولا تدعي شهادة أو نتائج مهنية مضمونة. هي أدوات ممارسة وأدلة جاهزية قابلة للمراجعة.</p>
              </div>
            </details>
          </div>
        </article>
'''

html = career.read_text(encoding='utf-8')
marker = '\n\n\n\n\n      </div>\n    </section>\n\n<section class="section" id="skill-modules">'
if marker not in html:
    marker = '\n\n\n      </div>\n    </section>\n\n<section class="section" id="skill-modules">'
if marker not in html:
    raise SystemExit('Insertion marker not found')
html = html.replace(marker, article + marker, 1)
html = html.replace('Book Tools 001–008: الثقة كأفعال صغيرة، تصفية الذهن، أنماط التفاعل، التفاوض بالتعاطف، المرونة التشغيلية، التوافق اليومي، هندسة الوقت والأولويات التشغيلية، وأدوات التركيز الكامل.',
                    'Book Tools 001–009: الثقة كأفعال صغيرة، تصفية الذهن، أنماط التفاعل، التفاوض بالتعاطف، المرونة التشغيلية، التوافق اليومي، هندسة الوقت والأولويات التشغيلية، أدوات التركيز الكامل، والقيادة المقصودة.')
career.write_text(html, encoding='utf-8')

idx = index.read_text(encoding='utf-8')
idx = idx.replace('Book Tools 001–008: الثقة كأفعال صغيرة، تصفية الذهن، أنماط التفاعل، التفاوض بالتعاطف، المرونة التشغيلية، التوافق اليومي، هندسة الوقت والأولويات التشغيلية، وأدوات التركيز الكامل.',
                  'Book Tools 001–009: الثقة كأفعال صغيرة، تصفية الذهن، أنماط التفاعل، التفاوض بالتعاطف، المرونة التشغيلية، التوافق اليومي، هندسة الوقت والأولويات التشغيلية، أدوات التركيز الكامل، والقيادة المقصودة.')
idx = idx.replace('Confidence + Clear-Mind + Interaction + Negotiation + Resilience + Performance + Time + Full Focus',
                  'Confidence + Clear-Mind + Interaction + Negotiation + Resilience + Performance + Time + Full Focus + Intentional')
idx = idx.replace('تحويل الكتب إلى أدوات عمل: بطاقة اجتماع، مواءمة توقعات، مراجعة أسبوعية، تخطيط تواصل، أسئلة تفاوض، توقف تكتيكي، سجل توافق يومي، ميزانية ساعات، وبطاقات SMARTER وBig 3 ومراجعة فصلية.',
                  'تحويل الكتب إلى أدوات عمل: بطاقة اجتماع، مواءمة توقعات، مراجعة أسبوعية، تخطيط تواصل، أسئلة تفاوض، توقف تكتيكي، سجل توافق يومي، ميزانية ساعات، بطاقات SMARTER وBig 3، وبطاقة مهمة ربعية مع مراجعة مهام منخفضة القيمة.')
index.write_text(idx, encoding='utf-8')

prompt = '''# Claude Fable Final Polish Prompt — v29 Book Tool 009

Task:
Review and lightly polish the static website after adding Book Tool 009: Intentional Leadership Routine, derived from Live Intentionally.

Hard constraints:
- Static HTML/CSS/JS only.
- Preserve Arabic RTL layout, mobile readability, Water Wonder pages, PDFs, and both contact emails.
- Do not use personal, family, age, or private context.
- Do not copy protected book passages; keep all content as transformed workplace tools.
- Do not claim certification, mastery, guaranteed outcomes, or confidential company results.
- Do not introduce the blocked career-outcome wording already removed from the site.

Check specifically:
1. career-os.html section #book-tool-009.
2. Index card text showing Book Tools 001–009.
3. Internal anchors and buttons.
4. Arabic clarity and concise card copy.
5. No overclaiming in CV/LinkedIn wording.

Return:
- Any exact lines you changed.
- Confirmation that all hard constraints passed.
'''
(root / 'CLAUDE_FABLE_V29_BOOK_TOOL_009_PROMPT.md').write_text(prompt, encoding='utf-8')

with changelog.open('a', encoding='utf-8') as f:
    f.write('\n\n## v29 — Book Tool 009 Intentional Leadership Routine\n')
    f.write('- Added Book Tool 009 derived from Live Intentionally: quarterly mission card, junk task audit, first 30 minutes, weekly pattern log, reframe sheet, direct feedback protocol, daily review, book-to-tool extraction, and values clarity.\n')
    f.write('- Updated index and Career-OS copy to show Book Tools 001–009.\n')
    f.write('- Added CLAUDE_FABLE_V29_BOOK_TOOL_009_PROMPT.md for final polish.\n')
