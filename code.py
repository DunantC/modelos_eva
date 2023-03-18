-cascade:
python3 demo.py --video-input videos/2023_01_10_154334_045.mp4 --output result/cascade --config-file configs/quick_schedules/cascade_mask_rcnn_R_50_FPN_inference_acc_test.yaml
key:3 --(4)
-python3 demo.py --video-input videos/2023_01_10_154334_045.mp4 --output result/key --config-file configs/quick_schedules/keypoint_rcnn_R_50_FPN_inference_acc_test.yaml
panoptic:2--
-python3 demo.py --video-input videos/2023_01_10_154334_045.mp4 --output result/panoptic --config-file configs/quick_schedules/panoptic_fpn_R_50_inference_acc_test.yaml
retinate 4 --(3)
-python3 demo.py --video-input videos/2023_01_10_154334_045.mp4 --output result/retinate --config-file configs/quick_schedules/retinanet_R_50_FPN_inference_acc_test.yaml
semantic 1 --
-python3 demo.py --video-input videos/2023_01_10_154334_045.mp4 --output result/semantic --config-file configs/quick_schedules/semantic_R_50_FPN_inference_acc_test.yaml


