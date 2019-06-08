# Retinal Fluids Segmentation from Optical Coherence Tomography Images

The vision formation in humans is due to human eyes. Human eye has three main layers i.e. the sclera, choroid and the retina. Retina is the innermost layer of an eye where the scaled and inverted vision is formed. Any damage to retina can cause severe visual impairment or even blindness. Retinal disorders are collectively known as retinopathy. Retinopathy can be easily visualized in early stages through optical coherence tomography (OCT) imagery. Retinal fluids are the prime cause of visual impairment and they are formed within the retina mainly because of diabetes. Retinal fluids are characterized as intra-retinal or sub-retinal depending upon their locality within the retina. Retinal fluids in one of the randomly selected OCT scans is shown below:

There are various publicly available OCT datasets which contains fluid annotations. One of the renown dataset is given by Vision and Image Processing Lab, Duke University at the following URL: [link](http://people.duke.edu/~sf59/Chiu_BOE_2014_dataset.htm) 

    http://people.duke.edu/~sf59/Chiu_BOE_2014_dataset.htm

The dataset contains around 610 OCT scans of 10 subjects suffering from severe diabetic macular edema (one of the most common retinal disorders). The dataset as well as the annotations are stored in 10 mat files (one for each subject). Each mat file contains ‘images’ matrix having the dimension as (496x768x61) where 496 are rows, 768 are columns and 61 are the total B-scans for the candidate subject. Similarly, the fluid annotations are given in the matrix named as ‘manualFluid1’ and ‘manualFluid2’ marked by the two clinicians. Note: ‘NaNs’ in the annotation denotes the area which has not been marked by the clinicians.

In this assignment, you need to extract the retinal fluids from the candidate B-scan using image processing and deep learning techniques. Then you need to evaluate the techniques using accuracy and the dice coefficient which can be computed through following formulas.

    Accuracy = (Tp + Tn) / (Tp + Tn + Fp + Fn)
    
where Tp are the true positives indicating that the fluid pixels extracted by the algorithm matches the ground truth, Tn are the true negatives indicating that the no-fluid pixels extracted by the algorithm matches the ground truth, Fp are the false positives indicating that the fluid pixels are incorrectly extracted by the algorithm and Fn are the false negatives indicating that the no-fluid pixels are incorrectly extracted by the algorithm. The dice coefficient can be computed through:

    DC = 2 (X ∩ Y) / (|X| + |Y|)
    
where X and Y denotes the extracted fluid and the ground truth respectively.

Two standard approaches are given to you below to extract retinal fluids. However, you have a freedom to develop your own algorithm as well but, in that case, you need to have a proper justification with quantitative measurements.

## Algorithm-1
- Read the OCT image
- Denoise the image and remove the acquisition noise
- Compute gradients w.r.t x and y direction
- Extract the top and bottom retinal layers
- Use the extracted retinal layers to generate a binary mask
- Multiply the binary mask with the original image to extract the retina
- After extracting the retina, use adaptive thresholding to extract the fluid region
- Compute the accuracy and the dice coefficient of the algorithm through the given formulas
- Compare this approach with Algorithm-2

## Algorithm-2
- Split the whole dataset into training and testing
- You have the liberty to choose the partition ratio, but the ideal way would be to keep 9 subjects
data for training and the 10th subject data for testing
- Develop a fully convolutional network (FCN), UNet or SegNet model for fluid segmentation
- Train the network
- After training the network, use it to extract retinal fluids from the OCT scan of 10th subject
- Compute the accuracy and the dice coefficient of the algorithm through the given formulas
- Compare this approach with Algorithm-1