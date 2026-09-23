# UAV-RSOD作者数据询问信（待审阅，未发送）

收件人：Rampriya R. S.，`rampriya.rs@vit.ac.in`。地址来源：数据论文公开XML的email字段；发送前可再次核对。发信人姓名、单位及邮箱尚未由用户确认，署名保留占位，不自动代填。

用途：询问原图标注、增强派生关系与来源分组；不是要求作者重新标注或承诺提供数据。未经用户明确授权不发送。

Subject: UAV-RSOD: original detection annotations and image provenance

Dear Dr. Rampriya and co-authors,

Thank you for releasing UAV-RSOD. I am assessing its suitability for a research project on time-budget-constrained detection of small known obstacles in railway UAV imagery.

I downloaded both archives from Zenodo record 12606374 and verified their published MD5 checksums. I could locate the 315 original images and segmentation masks in V1, and the augmented detection images and VOC annotations in V2. Could you please clarify whether the following resources are available?

1. Detection bounding boxes for the 315 unaugmented images, with matching filenames and coordinate conventions.
2. A mapping from each V2 image to its original image, together with the augmentation script and any saved transformation parameters or random states needed to reproduce the mapping. The article's code link appears to contain an mAP evaluation script; I may have missed a separate augmentation resource.
3. Source video or flight/session identifiers, frame numbers or timestamps, and information about repeated obstacle placements, so that related frames and augmented copies can be kept in the same evaluation group. If video sharing is restricted, a provenance table would still be useful.

I also found 1,611 training images and 391 test images in the archive, compared with 1,602/400 in the article. For example, test/1051.jpg and train/1829.jpg have identical file hashes. Is there a corrected split or guidance for constructing a source-separated evaluation?

Finally, could you clarify the coordinate scale and evaluation settings used for the small-object AP/AR columns in Table 3, and whether the small-object counts were measured before or after image resizing?

If these resources are not available, a clarification of the dataset's limitations would also help us plan an appropriate study. Please let me know the applicable access and reuse conditions for any additional materials.

Thank you for your time.

Best regards,

[Your name]

[Your affiliation]
